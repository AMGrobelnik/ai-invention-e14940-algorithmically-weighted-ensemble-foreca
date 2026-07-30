import json
import os

with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/full_data_out.json", "r") as f:
    full_data = json.load(f)

# Preview: 10 examples per dataset
preview_data = {"datasets": []}
for ds in full_data["datasets"]:
    preview_data["datasets"].append({
        "dataset": ds["dataset"],
        "examples": ds["examples"][:10]
    })
with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/preview_data_out.json", "w") as f:
    json.dump(preview_data, f, indent=2)

# Mini: 3 examples per dataset
mini_data = {"datasets": []}
for ds in full_data["datasets"]:
    mini_data["datasets"].append({
        "dataset": ds["dataset"],
        "examples": ds["examples"][:3]
    })
with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/mini_data_out.json", "w") as f:
    json.dump(mini_data, f, indent=2)

print("Variants generated successfully.")
