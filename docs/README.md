# Fractal Analysis of Financial Time Series

## Overview
This project investigates whether financial asset returns exhibit
statistically meaningful fractal or long-memory behaviour using the
Hurst exponent.

## Research Questions
- Do observed Hurst exponents differ significantly from those expected
  under random processes?
- Does the Hurst exponent vary through time?
- Are changes in Hurst associated with identifiable market regimes?
- Can rolling Hurst estimates provide useful features for predictive models?

## Data
Daily price data for 20 ETFs representing multiple asset classes.

## Methodology
1. Clean price data
2. Compute log returns
3. Estimate full-sample Hurst exponents
4. Compare estimates against null simulations
5. Compute rolling Hurst exponents
6. Analyze temporal variation and statistical significance

## Current Status
Rolling Hurst estimates have been computed using 252-trading-day windows.
Analysis of the resulting Hurst time series is in progress.

## Next Steps
- Analyze rolling Hurst distributions
- Develop appropriate rolling null comparisons
- Investigate regime behaviour
- Evaluate whether Hurst contains predictive information