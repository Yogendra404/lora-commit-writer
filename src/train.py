"""LoRA fine-tuning with PEFT + TRL."""
import json
import os
import torch
from datasets import load_dataset
from peft import LoraConfig
from transformers import AutoModelForCausalLM
from trl import SFTConfig, SFTTrainer

from common import (ADAPTER_DIR, BASE_MODEL, DATA_DIR, MAX_LEN, RESULTS_DIR,
                    get_dtype, load_tokenizer)

LORA_R = 8
LORA_ALPHA = 16
LORA_DROPOUT = 0.05
LEARNING_RATE = 2e-4
EPOCHS = 3
BATCH_SIZE = 2
GRAD_ACCUM = 8


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)
    tok = load_tokenizer()
    dtype = get_dtype()
    use_bf16 = dtype == torch.bfloat16

    train_ds = load_dataset("json", data_files=f"{DATA_DIR}/train.jsonl")["train"]
    val_ds = load_dataset("json", data_files=f"{DATA_DIR}/val.jsonl")["train"]
    print(f"model={BASE_MODEL} train={len(train_ds)} val={len(val_ds)} dtype={dtype}")

    model = AutoModelForCausalLM.from_pretrained(BASE_MODEL, torch_dtype=dtype)

    lora = LoraConfig(
        r=LORA_R,
        lora_alpha=LORA_ALPHA,
        lora_dropout=LORA_DROPOUT,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                        "gate_proj", "up_proj", "down_proj"],
        task_type="CAUSAL_LM",
    )

    kw = dict(
        output_dir="outputs",
        num_train_epochs=EPOCHS,
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        gradient_accumulation_steps=GRAD_ACCUM,
        learning_rate=LEARNING_RATE,
        lr_scheduler_type="cosine",
        warmup_steps=3,
        logging_steps=5,
        eval_strategy="steps",
        eval_steps=20,
        save_strategy="no",
        bf16=use_bf16,
        fp16=not use_bf16,
        gradient_checkpointing=True,
        gradient_checkpointing_kwargs={"use_reentrant": False},
        report_to="none",
        seed=42,
    )
    try:
        args = SFTConfig(**kw, max_length=MAX_LEN)
    except TypeError:
        args = SFTConfig(**kw, max_seq_length=MAX_LEN)

    trainer = SFTTrainer(model=model, args=args, train_dataset=train_ds,
                         eval_dataset=val_ds, peft_config=lora,
                         processing_class=tok)
    trainer.model.print_trainable_parameters()
    trainer.train()

    trainer.save_model(ADAPTER_DIR)
    tok.save_pretrained(ADAPTER_DIR)
    with open(f"{RESULTS_DIR}/training_log.json", "w") as f:
        json.dump(trainer.state.log_history, f, indent=2)
    print(f"Saved adapter to {ADAPTER_DIR}/")


if __name__ == "__main__":
    main()
