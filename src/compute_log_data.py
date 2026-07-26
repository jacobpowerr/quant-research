import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CLEANED_PRICES = PROJECT_ROOT / "data/clean/cleaned_prices.csv"

prices = pd.read_csv(
    CLEANED_PRICES,
    header=[0,1],
    index_col=0,
    parse_dates=True,
)

close_prices = prices["Close"]
log_prices = np.log(close_prices)
log_returns = log_prices.diff().dropna()

log_prices.to_csv(PROJECT_ROOT / "data/processed/log_prices.csv")
log_returns.to_csv(PROJECT_ROOT / "data/processed/log_returns.csv")
