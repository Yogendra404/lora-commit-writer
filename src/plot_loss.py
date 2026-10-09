"""Plot training/eval loss from results/training_log.json."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

log = json.load(open("results/training_log.json"))
tr = [(e["step"], e["loss"]) for e in log if "loss" in e]
ev = [(e["step"], e["eval_loss"]) for e in log if "eval_loss" in e]

plt.figure(figsize=(7, 4))
plt.plot(*zip(*tr), label="train loss")
if ev:
    plt.plot(*zip(*ev), marker="o", label="eval loss")
plt.xlabel("step"); plt.ylabel("loss"); plt.legend(); plt.grid(alpha=.3)
plt.title("LoRA fine-tuning loss")
plt.tight_layout()
plt.savefig("results/loss_curve.png", dpi=150)
print("Saved results/loss_curve.png")
