"""Shared settings and helpers."""
import os
import re
import torch
from transformers import AutoTokenizer

BASE_MODEL = os.environ.get("BASE_MODEL", "Qwen/Qwen2.5-1.5B-Instruct")
ADAPTER_DIR = "adapter"
DATA_DIR = "data"
RESULTS_DIR = "results"
MAX_LEN = 768          # tokens per training example
MAX_DIFF_CHARS = 1500  # diff characters kept per example

SYSTEM_PROMPT = (
    "You are a commit message writer. Given a git diff, reply with exactly one "
    "line: a Conventional Commit message (type(scope): summary). Output only the message."
)

TYPES = "feat|fix|docs|refactor|test|chore|perf|style|build|ci|revert"
CONV_RE = re.compile(rf"^({TYPES})(\([^)]+\))?!?: .+")


def user_prompt(diff: str) -> str:
    return f"Write a Conventional Commit message for this diff:\n\n{diff}"


def get_dtype():
    """bf16 if the GPU supports it, otherwise fp32 weights (+ fp16 autocast on T4)."""
    if torch.cuda.is_available() and torch.cuda.is_bf16_supported():
        return torch.bfloat16
    return torch.float32


def load_tokenizer():
    tok = AutoTokenizer.from_pretrained(BASE_MODEL)
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    return tok