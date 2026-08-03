import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "new_prices.csv"

df = pd.read_csv(RAW_DATA_PATH, 
                 header=[0, 1],
                 index_col=0,
                 parse_dates=True
)

close = df["Close"]

start_dates = {
    ticker: close[ticker].first_valid_index()
    for ticker in close.columns
}

common_start = max(start_dates.values())

df = df.loc[common_start:]

df.to_csv(PROJECT_ROOT / "data" / "processed" / "cleaned_prices.csv")

print(f"Shape : {df.shape}")
print(f"Total missing values: {df.isna().sum().sum()}")