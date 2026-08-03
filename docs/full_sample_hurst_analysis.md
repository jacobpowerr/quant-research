# Analysis of Full Sample Hurst Calcuation

## Objective
The intended purpose was to test to analyse wether hurst calculations on my chosen ETF's show any statistical significance when compared to IID Gaussian returns

## Method
Used 4463 days of log returns, across 20 ETF's. Used the compute_Hc function from the hurst library. Now for the null hypothesis I used 4463 days of normally distributed returns with a mean of 0 and a standard deviation of 1. I then calculated various other measurements and computed the p-value.

## Results
DBC and USO had unadjusted p-values around 0.026. But the Bonferroni threshold was 0.0025. All other results had 0.3-1 p-values.

## Interpretation
The apparent persistence in DBC and USO is insufficient to reject the null after correct for multiple comparisons.

## Limitatiosn
This null model is IID and Gaussian thus it does may not reproduce volatility clustering, heavy tails or other financial return properties.

## Conclusion
Although DBC and USO produced unadjusted p-values below 0.05, neither result remained statistically significant after applying the Bonferroni correction for 20 simultaneuos tests. Therefore, this analysis does not provide sufficient evidence that any asset's full-sample Hurst exponent differs from the IID Gaussian null at the family-wise 5% signifiance level.

