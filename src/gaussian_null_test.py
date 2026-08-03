from pathlib import Path

from hurst import compute_Hc
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
HURST_DATA = PROJECT_ROOT / "data/processed/hurst_results_log_returns.csv"

df = pd.read_csv(HURST_DATA)
observed_hurst = df["Hurst"]

def run_null_experiment(
        n_simulations: int,
        series_length: int,
        mean: float = 0.0,
        std: float = 1.0,
        seed: int = 42,
) -> np.ndarray:

    rng = np.random.default_rng(seed)
    estimates = np.empty(n_simulations)

    for simulation in range(n_simulations):
        test_returns = rng.normal (
            loc=mean,
            scale=std,
            size=series_length
        )

        H, _, _ = compute_Hc(
            test_returns,
            kind="change",
            simplified=False
        )

        estimates[simulation] = H

    return estimates

estimates = run_null_experiment(
    n_simulations=1000,
    series_length=4463,
)

def analyze_null_results(estimates, observed_hurst, PROJECT_ROOT):

    null_mean = np.mean(estimates)
    null_max = np.max(estimates)
    null_min = np.min(estimates)
    null_distance = np.abs(estimates - null_mean)
    p_values = []

    for hurst in observed_hurst:
        observed_distance = np.abs(hurst - null_mean)
        extreme_results = null_distance >= observed_distance
        extreme_count = np.sum(extreme_results)
        p_value = (extreme_count + 1) / (len(estimates) + 1)
        p_values.append(p_value)

    null_std = np.std(estimates, ddof=1)

    lower_95 = np.percentile(estimates, 2.5)
    upper_95 = np.percentile(estimates, 97.5)

    null_results = pd.DataFrame({
        "simulation": np.arange(1, len(estimates) + 1),
        "hurst": estimates,
    })

    null_results.to_csv(
        PROJECT_ROOT / "results/null_models/gaussian_null_estimates.csv"
    )

    hurst_significance = pd.DataFrame({
        "Asset": df["Ticker"],
        "Observed_hurst": observed_hurst,
        "Null_Mean": null_mean,
        "Null_Std": null_std,
        "Null_Min": null_min,
        "Null_Max": null_max,
        "Null_Lower_95": lower_95,
        "Null_Upper_95": upper_95,
        "P_Value": p_values,
    })

    hurst_significance.to_csv(
        PROJECT_ROOT / "results/null_models/hurst_significance.csv"
    ) 

    null_results.to_csv(
        PROJECT_ROOT / "results/null_models/gaussian_null_estimates.csv"
    )

    return hurst_significance

hurst_significance = analyze_null_results(
    estimates=estimates,
    observed_hurst=observed_hurst,
    PROJECT_ROOT=PROJECT_ROOT,
)

print(hurst_significance)

