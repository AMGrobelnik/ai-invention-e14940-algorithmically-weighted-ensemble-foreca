import numpy as np
import json
import os

os.makedirs("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets", exist_ok=True)
os.makedirs("/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results", exist_ok=True)

np.random.seed(42)
n_steps = 1000

# 1. Random noise
noise = np.random.normal(0, 1, n_steps).tolist()

# 2. Sinusoidal with drift
t = np.linspace(0, 50, n_steps)
sin_drift = (np.sin(t) + 0.05 * t + np.random.normal(0, 0.2, n_steps)).tolist()

# 3. Chaotic Lorenz system (simplified Euler integration)
xs, ys, zs = [1.0], [1.0], [1.0]
dt = 0.01
sigma, beta, rho = 10.0, 8.0/3.0, 28.0
for _ in range(n_steps - 1):
    x, y, z = xs[-1], ys[-1], zs[-1]
    dx = sigma * (y - x) * dt
    dy = (x * (rho - z) - y) * dt
    dz = (x * y - beta * z) * dt
    xs.append(x + dx)
    ys.append(y + dy)
    zs.append(z + dz)
lorenz = xs

# 4. Non-stationary AR(2)
ar_series = [0.0, 0.0]
for i in range(2, n_steps):
    phi1 = 0.5 + 0.3 * np.sin(i / 200.0)
    phi2 = -0.2 + 0.1 * np.cos(i / 300.0)
    val = phi1 * ar_series[-1] + phi2 * ar_series[-2] + np.random.normal(0, 0.5)
    ar_series.append(val)

datasets = {
    "random_noise": {"regime": "stochastic", "data": noise},
    "sinusoidal_drift": {"regime": "trend_seasonal", "data": sin_drift},
    "chaotic_lorenz": {"regime": "chaotic", "data": lorenz},
    "non_stationary_ar2": {"regime": "non_stationary", "data": ar_series}
}

for name, content in datasets.items():
    path = f"/ai-inventor/aii_data/runs/run_jv2O_AqFqWEi/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/temp/datasets/{name}.json"
    with open(path, "w") as f:
        json.dump(content, f)

print("Datasets successfully generated.")
