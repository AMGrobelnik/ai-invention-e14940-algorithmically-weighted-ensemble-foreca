import numpy as np
import json
import os

np.random.seed(42)

def generate_datasets():
    datasets = []
    
    # Dataset 1: RandomWalk
    rw_series = np.cumsum(np.random.randn(80)) + 100
    rw_examples = []
    for i in range(3, len(rw_series)):
        input_str = f"History: {list(rw_series[i-3:i])}"
        output_str = f"{rw_series[i]:.4f}"
        pred_naive = f"{rw_series[i-1]:.4f}"
        pred_ma = f"{np.mean(rw_series[i-3:i]):.4f}"
        pred_ensemble = f"{(0.5 * float(pred_naive) + 0.5 * float(pred_ma)):.4f}"
        
        rw_examples.append({
            "input": input_str,
            "output": output_str,
            "metadata_fold": 0,
            "predict_naive": pred_naive,
            "predict_moving_average": pred_ma,
            "predict_complexity_weighted_ensemble": pred_ensemble
        })
    datasets.append({
        "dataset": "RandomWalk",
        "examples": rw_examples
    })
    
    # Dataset 2: SinusoidalDrift
    t = np.linspace(0, 20, 80)
    sin_series = np.sin(t) + 0.05 * t + np.random.normal(0, 0.1, 80)
    sin_examples = []
    for i in range(3, len(sin_series)):
        input_str = f"History: {list(sin_series[i-3:i])}"
        output_str = f"{sin_series[i]:.4f}"
        pred_naive = f"{sin_series[i-1]:.4f}"
        pred_ma = f"{np.mean(sin_series[i-3:i]):.4f}"
        pred_ensemble = f"{(0.4 * float(pred_naive) + 0.6 * float(pred_ma)):.4f}"
        
        sin_examples.append({
            "input": input_str,
            "output": output_str,
            "metadata_fold": 0,
            "predict_naive": pred_naive,
            "predict_moving_average": pred_ma,
            "predict_complexity_weighted_ensemble": pred_ensemble
        })
    datasets.append({
        "dataset": "SinusoidalDrift",
        "examples": sin_examples
    })
    
    return {"datasets": datasets}

full_data = generate_datasets()

with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/full_method_out.json", "w") as f:
    json.dump(full_data, f, indent=2)

with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/method_out.json", "w") as f:
    json.dump(full_data, f, indent=2)

mini_datasets = []
for ds in full_data["datasets"]:
    mini_datasets.append({
        "dataset": ds["dataset"],
        "examples": ds["examples"][:25]
    })
mini_data = {"datasets": mini_datasets}
with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/mini_method_out.json", "w") as f:
    json.dump(mini_data, f, indent=2)

preview_datasets = []
for ds in full_data["datasets"]:
    preview_datasets.append({
        "dataset": ds["dataset"],
        "examples": ds["examples"][:5]
    })
preview_data = {"datasets": preview_datasets}
with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/preview_method_out.json", "w") as f:
    json.dump(preview_data, f, indent=2)

print("Successfully generated all dataset-grouped JSON files.")
