from pathlib import Path

import pandas as pd
from hurst import compute_Hc
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "processed"

WINDOW_SIZE = 252


log_returns = pd.read_csv(
    DATA_PATH / "log_returns.csv",
    index_col="Date",
    parse_dates=["Date"]
)

rolling_hurst = []

def estimate_hurst(returns):
    H, _, _ = compute_Hc(
        returns.to_numpy(),
        kind="change",
        simplified=False
    )
    return H

for end in range(WINDOW_SIZE, len(log_returns) + 1):
    window = log_returns.iloc[end - WINDOW_SIZE:end]
    window_end_date = window.index[-1]

    for ticker in log_returns.columns:
        ticker_returns = window[ticker].dropna()

        H = estimate_hurst(ticker_returns)

        rolling_hurst.append({
        "Date" : window_end_date,
        "Ticker": ticker,
        "Hurst" : H
        })


rolling_hurst_df = pd.DataFrame(rolling_hurst)

rolling_hurst_wide = rolling_hurst_df.pivot(
    index="Date",
    columns="Ticker",
    values="Hurst"
)

rolling_hurst_wide = rolling_hurst_wide.reset_index()

rolling_hurst_wide.to_csv(
    DATA_PATH / "rolling_hurst.csv",
    index=False
)