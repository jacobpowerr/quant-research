from pathlib import Path
import pandas as pd
import numpy as np

PARENT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PARENT_ROOT / "data/processed"

log_prices = pd.read_csv(
    DATA_PATH / "log_prices.csv",
    index_col="Date",
    parse_dates=["Date"]
)

regime_features = pd.read_csv(
    DATA_PATH / "regime_features.csv",
    parse_dates=["Date"]
)

HORIZON = 21

log_prices = log_prices.sort_index()

future_log_prices = log_prices.shift(-HORIZON)

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
    how="inner"
)

data["Current_Direction"] = np.sign(data["Momentum"])

data = data.dropna(subset=["Future_Direction"]).copy()

data = data[
    (data["Current_Direction"] != 0) &
    (data["Future_Direction"] != 0)
].copy()

data["Trend_Continuation"] = (
    data["Current_Direction"] == data["Future_Direction"]
).astype(int)

print(data["Trend_Continuation"].value_counts())
print(data["Trend_Continuation"].value_counts(normalize=True))

data = data.sort_values(["Ticker", "Date"])

data.to_csv(
    DATA_PATH / "model_data.csv",
    index=False
)