from scipy.optimize import minimize
import numpy as np
import pandas as pd

# Define expected returns and covariance matrix
returns = np.array([0.05, 0.1, 0.12, 0.07])
covariance = np.array([
    [0.01, 0.001, 0.005, 0.003],
    [0.001, 0.04, 0.002, 0.01],
    [0.005, 0.002, 0.09, 0.01],
    [0.003, 0.01, 0.01, 0.06]
])

# Define risk aversion parameter
risk_aversion = 1

# Define objective function to minimize portfolio variance


def portfolio_variance(weights, covariance):
    return np.dot(weights.T, np.dot(covariance, weights))

# Define objective function to maximize expected return


def portfolio_expected_return(weights, returns):
    return -np.dot(returns, weights)


# Define constraints: weights must sum to 1
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# Define bounds for weights
bounds = tuple((0, 1) for i in range(len(returns)))

# Minimize negative expected return subject to constraints and bounds
result = minimize(portfolio_expected_return, len(
    returns)*[1/len(returns)], args=(returns,), constraints=constraints, bounds=bounds)

weights = result.x

portfolio_return = np.dot(weights.T, returns)
portfolio_variance = portfolio_variance(weights, covariance)

sharpe_ratio = (portfolio_return - risk_free_rate) / \
    np.sqrt(portfolio_variance)

Print results
print("Optimal portfolio weights:", weights)
print("Portfolio expected return:", portfolio_return)
print("Portfolio variance:", portfolio_variance)
print("Sharpe ratio:", sharpe_ratio)
