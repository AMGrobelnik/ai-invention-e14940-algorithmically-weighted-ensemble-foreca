import json
import numpy as np

path = "/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets/sinusoidal_drift.json"
with open(path, "r") as f:
    data = json.load(f)["data"]

series = np.array(data)
train = series[:800]
test = series[800:]

# Naive last-value forecast
naive_preds = test[:-1]
naive_actuals = test[1:]
naive_mse = np.mean((naive_actuals - naive_preds) ** 2)

# 3-point moving average forecast
ma_preds = []
for i in range(len(test) - 1):
    window = series[800 + i - 2 : 800 + i + 1] if i >= 2 else np.concatenate([train[-2+i:], test[:i+1]])
    ma_preds.append(np.mean(window))

ma_mse = np.mean((naive_actuals - np.array(ma_preds)) ** 2)

print(f"Naive MSE: {naive_mse:.4f}")
print(f"3-pt MA MSE: {ma_mse:.4f}")

results = {
    "naive_mse": float(naive_mse),
    "ma_mse": float(ma_mse),
    "better": "moving_average" if ma_mse < naive_mse else "naive"
}

with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/evaluation.json", "w") as f:
    json.dump(results, f, indent=2)
