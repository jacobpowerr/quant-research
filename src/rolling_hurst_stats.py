from pathlib import Path

import pandas as pd
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data/processed"

rolling_hurst = pd.read_csv(
    DATA_PATH / "rolling_hurst.csv"
    index="Date",
    parse_dates=["Date"]
)

