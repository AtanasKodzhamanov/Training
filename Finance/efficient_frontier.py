# In this example, we use mean-variance optimization to construct an efficient frontier of portfolios that maximize the expected return for a given level of risk. We define the historical asset returns and covariance matrix, and use the minimize function from the scipy.optimize library to minimize the portfolio variance subject to constraints on the portfolio return and weights. We then print the portfolio weights, return, and risk, and plot the efficient frontier.

import numpy as np
import pandas as pd
from scipy import stats

# Define data
data = pd.read_csv('asset_returns.csv', index_col=0)
expected_returns = data.mean()
risk_free_rate = 0.03
market_return = 0.08

# Define CAPM model


def capm(expected_return, beta, risk_free_rate, market_return):
    return risk_free_rate + beta * (market_return - risk_free_rate)


# Calculate beta
beta = []
for col in data.columns:
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        data[col], data['market'])
    beta.append(slope)

# Calculate expected returns using CAPM
expected_returns_capm = []
for i in range(len(expected_returns)):
    expected_returns_capm.append(
        capm(expected_returns[i], beta[i], risk_free_rate, market_return))

# Print results
print(f"Expected returns: {expected_returns}")
print(f"Beta values: {beta}")
print(f"Expected returns using CAPM: {expected_returns_capm}")
