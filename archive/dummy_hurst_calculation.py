import numpy as np

window_size = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

for seed in range(50):
    np.random.seed(seed)
    returns = np.random.normal(0, 1, 5000)

    rescaled_ranges = []

    for size in window_size:
        current_returns = returns[:size]
        mean = np.mean(current_returns)
        centered = current_returns - mean
        cum_dev = np.cumsum(centered)

        current_range = np.max(cum_dev) - np.min(cum_dev)
        standard_deviation = np.std(current_returns)

        rescaled_ranges.append(current_range / standard_deviation)

    hurst, intercept = np.polyfit(
        np.log(window_size),
        np.log(rescaled_ranges),
        1
    )

    print(seed, hurst)