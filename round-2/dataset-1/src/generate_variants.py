import json

with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/full_data_out.json", "r") as f:
    full_data = json.load(f)

preview_data = {
    "datasets": []
}

for ds in full_data["datasets"]:
    preview_data["datasets"].append({
        "dataset": ds["dataset"],
        "examples": ds["examples"][:5]
    })

with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/preview_data_out.json", "w") as f:
    json.dump(preview_data, f, indent=2)

mini_data = {
    "datasets": []
}

for ds in full_data["datasets"]:
    mini_data["datasets"].append({
        "dataset": ds["dataset"],
        "examples": ds["examples"][:50]
    })

with open("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/mini_data_out.json", "w") as f:
    json.dump(mini_data, f, indent=2)

print("Generated preview and mini datasets successfully.")
