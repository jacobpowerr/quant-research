from hurst import compute_Hc
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_FILES = PROJECT_ROOT / "data/processed"

log_returns = pd.read_csv(
    PROCESSED_FILES / "log_prices.csv",
    index_col="Date",
    parse_dates=["Date"]
)

results = []

for ticker in log_returns.columns:
    ticker_returns = log_returns[ticker].dropna()
    H, c, data = compute_Hc(
        ticker_returns,
        kind="price",
        simplified=False
    )

    print(f"{ticker} : H = {H:.4f}")

    results.append({
        "Ticker": ticker,
        "Hurst" : H
    })

hurst_df = pd.DataFrame(results)

hurst_df.to_csv(
    PROCESSED_FILES / "hurst_results_log_prices.csv",
    index=False)