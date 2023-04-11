# Portfolio optimization is the process of selecting the optimal mix of assets to achieve a desired level of risk and return. The goal of portfolio optimization is to construct a portfolio that maximizes the expected return for a given level of risk, or minimizes the risk for a given level of expected return. The process involves analyzing historical asset returns, estimating their expected future returns and volatility, and using mathematical models such as mean-variance optimization or the Capital Asset Pricing Model (CAPM) to construct an efficient frontier of portfolios.

# Mean-variance optimization is a popular portfolio optimization technique that was introduced by Harry Markowitz in 1952. The technique involves constructing an efficient frontier of portfolios that maximize the expected return for a given level of risk or minimize the risk for a given level of expected return. The efficient frontier is the set of portfolios that offer the highest expected return for a given level of risk, or the lowest risk for a given level of expected return.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Define data
data = pd.read_csv('asset_returns.csv', index_col=0)
expected_returns = data.mean()
cov_matrix = data.cov()

# Define objective function


def portfolio_variance(weights, cov_matrix):
    return np.dot(weights.T, np.dot(cov_matrix, weights))

# Define constraints


def portfolio_return(weights, expected_returns, target_return):
    return np.dot(weights.T, expected_returns) - target_return


constraints = [{'type': 'eq', 'fun': portfolio_return, 'args': (expected_returns, 0.1)},
               {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]

# Define bounds
bounds = [(0, 1) for i in range(len(expected_returns))]

# Define initial guess
x0 = np.ones(len(expected_returns)) / len(expected_returns)

# Optimize portfolio
result = minimize(portfolio_variance, x0, args=(cov_matrix,),
                  method='SLSQP', bounds=bounds, constraints=constraints)

# Print results
print(f"Portfolio weights: {result.x}")
print(f"Portfolio return: {np.dot(result.x, expected_returns):.2%}")
print(f"Portfolio risk (standard deviation): {np.sqrt(result.fun):.2%}")

# Plot efficient frontier
target_returns = np.linspace(
    expected_returns.min(), expected_returns.max(), 100)
portfolio_risks = []
for target_return in target_returns:
    constraint = {'type': 'eq', 'fun': portfolio_return,
                  'args': (expected_returns, target_return)}
    result = minimize(portfolio_variance, x0, args=(cov_matrix,), method='SLSQP', bounds=bounds, constraints=[
                      constraint, {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}])
    portfolio_risks.append(np.sqrt(result.fun))
plt.plot(portfolio_risks, target_returns)
plt.xlabel('Risk (Standard Deviation)')
plt.ylabel('Expected Return')
plt.title('Efficient Frontier')
plt.show()
