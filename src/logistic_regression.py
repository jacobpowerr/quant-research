from pathlib import Path
import pandas as pd
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "model_data.csv"

df = pd.read_csv(
    DATA_PATH,
    parse_dates = ["Date"]
)

print(df.head())
print(df.columns)
print(df.shape)
print(df.dtypes)