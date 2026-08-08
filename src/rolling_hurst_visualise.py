from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data/processed"

rolling_hurst = pd.read_csv(
    DATA_PATH / "rolling_hurst.csv",
    parse_dates=["Date"]
)

plt.figure(figsize=(12, 6))

plt.plot(rolling_hurst["Date"], rolling_hurst["USO"])

plt.axhline(
    y=0.5,
    linestyle="--",
    label="Random baseline"
)

plt.xlabel("Date")
plt.ylabel("Hust Exponent")
plt.title("Rolling Hurst Exponent - SPY")

plt.legend()
plt.grid()

plt.show()