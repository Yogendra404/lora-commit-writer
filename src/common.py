"""Shared settings and helpers."""
import os
import re
import torch
from transformers import AutoTokenizer

BASE_MODEL = os.environ.get("BASE_MODEL", "Qwen/Qwen2.5-0.5B-Instruct")
ADAPTER_DIR = "adapter"
DATA_DIR = "data"
RESULTS_DIR = "results"
MAX_LEN = 768
MAX_DIFF_CHARS = 1500

SYSTEM_PROMPT = (
    "You are a commit message writer. Given a git diff, reply with exactly one "
    "line: a Conventional Commit message (type(scope): summary). Output only the message."
)

TYPES = "feat|fix|docs|refactor|test|chore|perf|style|build|ci|revert"
CONV_RE = re.compile(rf"^({TYPES})(\([^)]+\))?!?: .+")


def user_prompt(diff: str) -> str:
    return f"Write a Conventional Commit message for this diff:\n\n{diff}"


def get_dtype():
    # bf16 only on Ampere+ GPUs (capability >= 8); T4 uses fp32 weights + fp16 autocast
    if torch.cuda.is_available() and torch.cuda.get_device_capability()[0] >= 8:
        return torch.bfloat16
    return torch.float32


def load_tokenizer():
    tok = AutoTokenizer.from_pretrained(BASE_MODEL)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    return tok
