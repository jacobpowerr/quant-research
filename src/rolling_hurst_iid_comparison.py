from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_PATH = PROJECT_ROOT / "data/processed"

metrics = ["mean", "std", "min", "max"]

etf_results = pd.read_csv(PROCESSED_PATH / "etf_rolling_hurst_metrics.csv")
iid_metrics = pd.read_csv(PROCESSED_PATH / "iid_rolling_hurst.csv")

for metric in metrics:

    null_mean = iid_results[metric].mean()

    for i in range(len(etf_results)):

        etf_value = etf_results.loc[i, metric]

        distance = etf_value - null_mean