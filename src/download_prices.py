import yfinance as yf
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

metadata = pd.read_csv(PROJECT_ROOT / "data" / "metadata"/ "asset_metadata.csv")

tickers = metadata["Ticker"].tolist()

price_data = yf.download(tickers, start="2000-01-01", end="2025-01-01",
interval="1d", auto_adjust=True)

price_data.to_csv("raw_prices.csv")