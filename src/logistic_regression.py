from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss, roc_auc_score

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "model_data.csv"

df = pd.read_csv(
    DATA_PATH,
    parse_dates = ["Date"]
)

df = df.sort_values(["Date", "Ticker"]).reset_index(drop=True)

required_columns = [
    "Ticker",
    "Date",
    "Trend_Continuation",
    "Hurst",
    "Volatility",
    "Momentum",
]

unique_dates = df["Date"].drop_duplicates().sort_values().to_numpy()

train_end = int(len(unique_dates) * 0.70)
validation_end = int(len(unique_dates) * 0.85)

gap = 21

train_dates = unique_dates[:train_end - gap]
validation_dates = unique_dates[train_end: validation_end - gap]
test_dates = unique_dates[validation_end:]

train_df = df[df["Date"].isin(train_dates)]
validation_df = df[df["Date"].isin(validation_dates)]
test_df = df[df["Date"].isin(test_dates)]

BASELINE_FEATURES = ["Volatility", "Momentum"]
HURST_FEATURES = ["Volatility", "Momentum", "Hurst"]
TARGET = "Trend_Continuation"

X_train_baseline = train_df[BASELINE_FEATURES]
X_train_hurst = train_df[HURST_FEATURES]
y_train = train_df[TARGET]

baseline_scaler = StandardScaler()
hurst_scaler = StandardScaler()

X_train_baseline_scaled = baseline_scaler.fit_transform(X_train_baseline)
X_train_hurst_scaled = hurst_scaler.fit_transform(X_train_hurst)

X_validation_baseline = validation_df[BASELINE_FEATURES]
X_validation_hurst = validation_df[HURST_FEATURES]
y_validation = validation_df[TARGET]

X_validation_baseline_scaled = baseline_scaler.transform(X_validation_baseline)
X_validation_hurst_scaled = hurst_scaler.transform(X_validation_hurst)

X_test_baseline = test_df[BASELINE_FEATURES]
X_test_hurst = test_df[HURST_FEATURES]
y_test = test_df[TARGET]

X_test_baseline_scaled = baseline_scaler.transform(X_test_baseline)
X_test_hurst_scaled = hurst_scaler.transform(X_test_hurst)

baseline_model = LogisticRegression(max_iter=1000)
hurst_model = LogisticRegression(max_iter=1000)

baseline_model.fit(X_train_baseline_scaled, y_train)
hurst_model.fit(X_train_hurst_scaled, y_train)

baseline_validation_probs = baseline_model.predict_proba(X_validation_baseline_scaled)[:, 1]

hurst_validation_probs = hurst_model.predict_proba(X_validation_hurst_scaled)[:, 1]

baseline_validation_loss = log_loss(y_validation, baseline_validation_probs)

hurst_validation_loss = log_loss(y_validation, hurst_validation_probs)

baseline_validation_auc = roc_auc_score(y_validation, baseline_validation_probs)

hurst_validation_auc = roc_auc_score(y_validation, hurst_validation_probs)

baseline_validation_predictions = (baseline_validation_probs >= 0.5).astype(int)

hurst_validation_predictions = (hurst_validation_probs >= 0.5).astype(int)

baseline_accuracy = accuracy_score(y_validation, baseline_validation_predictions)

hurst_accuracy = accuracy_score(y_validation, hurst_validation_predictions)

basleine_test_probs = baseline_model.predict_proba(X_test_baseline_scaled)[:, 1]

hurst_test_probs = hurst_model.predict_proba(X_test_hurst_scaled)[:, 1]

baseline_test_predictions = (basleine_test_probs >= 0.5).astype(int)

hurst_test_predictions = (hurst_test_probs >= 0.5).astype(int)

baseline_test_accuracy = accuracy_score(y_test, baseline_test_predictions)

hurst_test_accuracy = accuracy_score(y_test, hurst_test_predictions)

print(f"Naive Test Accuracy: {y_test.value_counts(normalize=True).max():.4f}")

print(f"Baseline Test Log loss: {log_loss(y_test, basleine_test_probs):.4f}")
print(f"Hurst Test Log loss: {log_loss(y_test, hurst_test_probs):.4f}")

print(f"Baseline Test AUC: {roc_auc_score(y_test, basleine_test_probs):.4f}")
print(f"Hurst Test AUC: {roc_auc_score(y_test, hurst_test_probs):.4f}")

print(f"Baseline Test Accuracy: {baseline_test_accuracy:.4f}")
print(f"Hurst Test Accuracy: {hurst_test_accuracy:.4f}")