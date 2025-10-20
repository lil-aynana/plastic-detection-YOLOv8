import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to your training results
run_dir = "runs/train/plastic_detection7"  # change if different
csv_path = os.path.join(run_dir, "results.csv")

# Load CSV
df = pd.read_csv(csv_path)

# --- Plot Losses ---
plt.figure(figsize=(8,5))
plt.plot(df["epoch"], df["train/box_loss"], label="Train Box Loss")
plt.plot(df["epoch"], df["train/cls_loss"], label="Train Class Loss")
if "val/box_loss" in df.columns:
    plt.plot(df["epoch"], df["val/box_loss"], label="Validation Box Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training & Validation Loss Over Epochs")
plt.legend()
plt.grid(True)
plt.show()

# --- Plot mAP, Precision, Recall ---
plt.figure(figsize=(8,5))
plt.plot(df["epoch"], df["metrics/precision(B)"], label="Precision")
plt.plot(df["epoch"], df["metrics/recall(B)"], label="Recall")
plt.plot(df["epoch"], df["metrics/mAP50(B)"], label="mAP@50")
plt.plot(df["epoch"], df["metrics/mAP50-95(B)"], label="mAP@50-95")
plt.xlabel("Epoch")
plt.ylabel("Score")
plt.title("Performance Metrics Over Epochs")
plt.legend()
plt.grid(True)
plt.show()
