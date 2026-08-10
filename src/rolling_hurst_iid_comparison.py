from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_PATH = PROJECT_ROOT / "data/processed"

metrics = ["mean", "std", "min", "max"]

etf_results = pd.read_csv(PROCESSED_PATH / "etf_rolling_hurst_metrics.csv")
iid_results = pd.read_csv(PROCESSED_PATH / "iid_rolling_hurst.csv")

comparison_results = []

for metric in metrics:

    null_mean = iid_results[metric].mean()
    null_std = iid_results[metric].std()

    for i in range(len(etf_results)):

        etf = etf_results.loc[i, "Ticker"]
        etf_value = etf_results.loc[i, metric]

        distance = etf_value - null_mean

        z_score = distance / null_std

        observed_distance = abs(distance)

        null_distances = abs(
            iid_results[metric] - null_mean
        )

        extreme_count = (
            null_distances >= observed_distance
        ).sum()

        p_value = (
            (extreme_count + 1) / (len(null_distances) + 1)
        )

        comparison_results.append({
            "Ticker": etf,
            "Metric": metric,
            "ETF_Value": etf_value,
            "Null_Mean": null_mean,
            "Distance": distance,
            "Z_Score": z_score,
            "P_Value": p_value
        })

comparison_df = pd.DataFrame(comparison_results)

pd.set_option("display.float_format", "{:.6f}".format)

mean_results = comparison_df[
    comparison_df["Metric"] == "mean"
].sort_values("P_Value")

print(mean_results[
    ["Ticker", "ETF_Value", "Null_Mean",
     "Distance", "Z_Score", "P_Value"]
     ])

std_results = comparison_df[
    comparison_df["Metric"] == "std"
].sort_values("P_Value")

print(std_results.to_string(index=False))