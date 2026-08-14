from pathlib import Path
import pandas as pd
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DATA = PROJECT_ROOT / "data/processed"

rolling_hurst = pd.read_csv(PROCESSED_DATA / "rolling_hurst.csv")
log_returns = pd.read_csv(
    PROCESSED_DATA / "log_returns.csv",
    parse_dates=["Date"],
    index_col="Date"
)
log_prices = pd.read_csv(
    PROCESSED_DATA / "log_prices.csv",
    parse_dates=["Date"],
    index_col="Date"
)

volatility = log_returns.rolling(window=252).std()
momentum = log_prices - log_prices.shift(63)

volatility = (
    volatility
    .reset_index()
    .melt(
        id_vars="Date",
        var_name="Ticker",
        value_name="Volatility"
    )
)

momentum = (
    momentum
    .reset_index()
    .melt(
        id_vars="Date",
        var_name="Ticker",
        value_name="Momentum"
    )
)

rolling_hurst = (
    rolling_hurst.melt(
        id_vars="Date",
        var_name="Ticker",
        value_name="Hurst"
    )
)

rolling_hurst["Date"] = pd.to_datetime(rolling_hurst["Date"])

features = rolling_hurst.merge(
    volatility,
    on=["Date", "Ticker"],
    how="inner"
)

features = features.merge(
    momentum,
    on=["Date", "Ticker"],
    how="inner"
)

features = features.dropna()

features.to_csv(
    PROJECT_ROOT / PROCESSED_DATA / "regime_features.csv",
    index=False
)