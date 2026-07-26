"""
Validate the hurst package on simulated Gaussian white noise.

Purpose:
- Estimate the finite-sample distribution of the Hurst exponent.
- Verify that the estimator behaves as expected before analysing market data.

Results (100 simulations, n=5000):
Mean H = 0.5408
Std H  = 0.0288
"""

from hurst import compute_Hc
import numpy as np

rng = np.random.default_rng(42)
estimates = []

for _ in range(100):
    test_returns = rng.normal(0, 1, 5000)

    H, c, data = compute_Hc(
        test_returns,
        kind="change",
        simplified=False
    )

    estimates.append(H)

print(f"Mean H: {np.mean(estimates):.4f}")
print(f"Std H:  {np.std(estimates):.4f}")
print(f"Min H:  {np.min(estimates):.4f}")
print(f"Max H:  {np.max(estimates):.4f}")