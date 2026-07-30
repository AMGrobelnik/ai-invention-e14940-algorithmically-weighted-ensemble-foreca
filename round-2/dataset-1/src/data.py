import json
import os
import numpy as np

# Load the generated datasets
input_dir = "/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets"
dataset_files = os.listdir(input_dir)

datasets_list = []

for file_name in dataset_files:
    if not file_name.endswith(".json"):
        continue
    ds_name = file_name.replace(".json", "")
    with open(os.path.join(input_dir, file_name), "r") as f:
        content = json.load(f)
    
    regime = content.get("regime", "unknown")
    raw_data = content.get("data", [])
    
    examples = []
    for idx, val in enumerate(raw_data):
        # Create input features (e.g. previous values or index) and target
        input_val = float(raw_data[idx - 1]) if idx > 0 else 0.0
        output_val = float(val)
        
        example = {
            "input": json.dumps({"previous_value": input_val, "time_index": idx}),
            "output": str(output_val),
            "metadata_regime": regime,
            "metadata_row_index": idx
        }
        examples.append(example)
        
    datasets_list.append({
        "dataset": ds_name,
        "examples": examples
    })

output_data = {
    "datasets": datasets_list
}

output_path = "/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/full_data_out.json"
with open(output_path, "w") as f:
    json.dump(output_data, f, indent=2)

print(f"Successfully standardized {len(datasets_list)} datasets to {output_path}")
