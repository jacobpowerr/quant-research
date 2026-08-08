import numpy as np
import pandas as pd
from pathlib import Path
from hurst import compute_Hc

WINDOW_SIZE = 252
SEED = 42
SERIES_LENGTH = 4463
N_SIMULATIONS = 100

def estimate_hurst(returns):
    H, _, _ = compute_Hc(
        returns,
        kind="change",
        simplified=False
    )
    return H

rng = np.random.default_rng(SEED)

null_means = []
null_stds = []
null_maxs = []
null_mins = []

for sim in range(N_SIMULATIONS):

    if sim % 10 == 0:
        print(f"Simulation {sim}/{N_SIMULATIONS}")

    iid_returns = rng.normal(
        loc=0,
        scale=1,
        size=SERIES_LENGTH
    )

    rolling_hurst = []

    for end in range(WINDOW_SIZE, len(iid_returns) + 1):

        window = iid_returns[end - WINDOW_SIZE:end]

        H = estimate_hurst(window)

        rolling_hurst.append(H)


    rolling_hurst = np.array(rolling_hurst)

    null_means.append(rolling_hurst.mean())
    null_stds.append(rolling_hurst.std())
    null_mins.append(rolling_hurst.min())
    null_maxs.append(rolling_hurst.max())

print("Null mean H:", np.mean(null_means))
print("Null mean std:", np.std(null_means))

print(
    "95 percent interval for mean H:",
    np.quantile(null_means, [0.025, 0.975])
)