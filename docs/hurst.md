1. Compute the log returns and the log prices
2. Then will compute the hurst of each and compare them
3. Each window size is multiplied by 2, to create a symmetry.
4. First tested my hurst algirthm on a dummy set before moving on to my real processed data
5. compute_hc function works correctly on random data, producing a result of H roughly = 0.54
6. Thus a random walk takes the value of H = 0.54 in my calculations