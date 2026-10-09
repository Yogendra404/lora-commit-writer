"""Run the SAME held-out prompts through base and fine-tuned model."""
import json
import re
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM

from common import (ADAPTER_DIR, BASE_MODEL, CONV_RE, DATA_DIR, RESULTS_DIR,
                    get_dtype, load_tokenizer)

N_PROMPTS = 20


def generate(model, tok, messages):
    text = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tok(text, return_tensors="pt").to(model.device)
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=60, do_sample=False,
                             pad_token_id=tok.pad_token_id)
    return tok.decode(out[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()


def ctype(s):
    m = re.match(r"^(\w+)", s)
    return m.group(1) if m else ""


def main():
    tok = load_tokenizer()
    base = AutoModelForCausalLM.from_pretrained(BASE_MODEL, torch_dtype=get_dtype(),
                                                device_map="auto")
    model = PeftModel.from_pretrained(base, ADAPTER_DIR)
    model.eval()

    rows = [json.loads(l) for l in open(f"{DATA_DIR}/test.jsonl")][:N_PROMPTS]
    results = []
    for r in rows:
        with model.disable_adapter():
            b = generate(model, tok, r["prompt"])
        t = generate(model, tok, r["prompt"])
        results.append({"diff": r["prompt"][1]["content"],
                        "reference": r["completion"][0]["content"],
                        "base": b, "finetuned": t})
        print(f"[{len(results)}/{len(rows)}] base: {b[:70]!r} | ft: {t[:70]!r}")

    def stats(key):
        fmt = sum(bool(CONV_RE.match(x[key].split("\n")[0])) for x in results)
        typ = sum(ctype(x[key]) == ctype(x["reference"]) for x in results)
        one = sum("\n" not in x[key] for x in results)
        n = len(results)
        return fmt / n, typ / n, one / n

    bs, fs = stats("base"), stats("finetuned")
    summary = (
        "| Metric | Base | Fine-tuned |\n|---|---|---|\n"
        f"| Valid Conventional Commit format | {bs[0]:.0%} | {fs[0]:.0%} |\n"
        f"| Commit type matches reference | {bs[1]:.0%} | {fs[1]:.0%} |\n"
        f"| Single-line output | {bs[2]:.0%} | {fs[2]:.0%} |\n"
    )

    md = [f"# Before/After comparison ({len(results)} held-out prompts)\n", summary, "\n---\n"]
    for i, x in enumerate(results, 1):
        md.append(f"## Example {i}\n```diff\n{x['diff'][:400]}\n...\n```\n"
                  f"- **Reference:** `{x['reference']}`\n"
                  f"- **Base:** {x['base']!r}\n"
                  f"- **Fine-tuned:** {x['finetuned']!r}\n")
    with open(f"{RESULTS_DIR}/comparison.md", "w") as f:
        f.write("\n".join(md))
    with open(f"{RESULTS_DIR}/comparison.json", "w") as f:
        json.dump(results, f, indent=2)
    print(summary)


if __name__ == "__main__":
    main()
