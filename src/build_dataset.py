"""Mine (diff -> commit message) pairs from real git repos."""
import argparse
import json
import random
import subprocess
import tempfile
from pathlib import Path

from common import CONV_RE, DATA_DIR, MAX_DIFF_CHARS, SYSTEM_PROMPT, user_prompt

EXCLUDES = [":(exclude)*.lock", ":(exclude)*lock.json", ":(exclude)*.min.js",
            ":(exclude)*.svg", ":(exclude)*.snap"]


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, errors="replace")
    return r.stdout


def mine_repo(path, limit):
    log = run(["git", "log", "--no-merges", "-n", str(limit * 6),
               "--format=%H%x1f%s"], cwd=path)
    pairs = []
    for line in log.splitlines():
        if "\x1f" not in line:
            continue
        sha, subject = line.split("\x1f", 1)
        subject = subject.strip()
        if not CONV_RE.match(subject) or len(subject) > 100:
            continue
        diff = run(["git", "show", "--format=", "--patch", "-U1", "--no-color",
                    sha, "--", "."] + EXCLUDES, cwd=path).strip()
        if len(diff) < 50:
            continue
        pairs.append((diff[:MAX_DIFF_CHARS], subject))
        if len(pairs) >= limit:
            break
    return pairs


def to_record(diff, msg):
    return {
        "prompt": [{"role": "system", "content": SYSTEM_PROMPT},
                   {"role": "user", "content": user_prompt(diff)}],
        "completion": [{"role": "assistant", "content": msg}],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos", nargs="+", required=True)
    ap.add_argument("--per-repo", type=int, default=200)
    args = ap.parse_args()

    all_pairs = []
    with tempfile.TemporaryDirectory() as tmp:
        for i, repo in enumerate(args.repos):
            path = repo
            if repo.startswith("http"):
                path = str(Path(tmp) / f"repo{i}")
                print(f"Cloning {repo} ...")
                subprocess.run(["git", "clone", "--quiet", "--depth", "1500", repo, path],
                               check=True)
            pairs = mine_repo(path, args.per_repo)
            print(f"{repo}: kept {len(pairs)} pairs")
            all_pairs += pairs

    seen, unique = set(), []
    for d, m in all_pairs:
        if (d, m) not in seen:
            seen.add((d, m))
            unique.append((d, m))

    random.Random(42).shuffle(unique)
    n = len(unique)
    n_test, n_val = max(20, n // 10), max(20, n // 10)
    splits = {"test": unique[:n_test],
              "val": unique[n_test:n_test + n_val],
              "train": unique[n_test + n_val:]}

    Path(DATA_DIR).mkdir(exist_ok=True)
    for name, items in splits.items():
        with open(f"{DATA_DIR}/{name}.jsonl", "w") as f:
            for d, m in items:
                f.write(json.dumps(to_record(d, m)) + "\n")
        print(f"{name}: {len(items)} examples")


if __name__ == "__main__":
    main()
