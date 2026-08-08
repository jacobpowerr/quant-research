from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data/processed"

rolling_hurst = pd.read_csv(
    DATA_PATH / "rolling_hurst.csv",
    parse_dates=["Date"]
)

hurst_summary = rolling_hurst.set_index("Date").describe().T

print(hurst_summary)