from hurst import compute_Hc
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_FILES = PROJECT_ROOT / "data/processed"

log_returns = pd.read_csv(
    PROCESSED_FILES / "log_returns.csv",
    header=[0,1],
    index_col=0,
    parse_dates=True
)

spy = log_returns["SPY"].dropna()

H, c, data = compute_Hc(
    spy,
    kind="change",
    simplified=False
)

print(f"Hurst exponent: {H:.4f}")
print(f"Scaling constant: {c:.4f}")