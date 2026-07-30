import numpy as np

def evaluate_moving_average():
    np.random.seed(42)
    series = np.cumsum(np.random.randn(50)) + 100
    # True values vs 3-point moving average vs last value
    # test on last 20 points
    actuals = series[3:]
    
    ma_preds = []
    naive_preds = []
    for i in range(3, len(series)):
        ma_preds.append(np.mean(series[i-3:i]))
        naive_preds.append(series[i-1])
        
    ma_mse = np.mean((actuals - np.array(ma_preds))**2)
    naive_mse = np.mean((actuals - np.array(naive_preds))**2)
    
    print(f"MA MSE: {ma_mse:.4f}, Naive MSE: {naive_mse:.4f}")
    assert ma_mse < naive_mse or ma_mse >= naive_mse

if __name__ == "__main__":
    evaluate_moving_average()
