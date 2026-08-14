from pathlib import Path
import pandas as pd
import numpy as np

PARENT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PARENT_ROOT / "data/processed"

log_prices = pd.read_csv(
    DATA_PATH / "log_prices.csv",
    index_col="Date",
    parse_dates="Date"
)

regime_features = pd.read_csv(
    DATA_PATH / "regime_features.csv",
    index_col="Date",
    parse_dates="Date"
)

HORIZON = 21

log_prices = log_prices.sort_index()

future_log_prices = log_prices(-HORIZON)

future_movement = future_log_prices - log_prices

future_direction = np.sign(future_movement)

future_direction_long = (
    future_direction
    .reset_index()
    .melt(
        id_vars="Date",
        var_name="Ticker",
        value_name="Future_Direction"
    )
)

data = regime_features.merge(
    future_direction_long,
    on=["Date", "Ticker"],
    how="innner"
)