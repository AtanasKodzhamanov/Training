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

# Define objective function to minimize portfolio variance


def portfolio_variance(weights, covariance):
    return np.dot(weights.T, np.dot(covariance, weights))


# Define constraints: weights must sum to 1, and each weight must be non-negative
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
               {'type': 'ineq', 'fun': lambda x: x})

# Define bounds for weights
bounds = tuple((0, 1) for i in range(len(returns)))

# Minimize portfolio variance subject to constraints
result = minimize(portfolio_variance, len(
    returns)*[1/len(returns)], args=(covariance,), constraints=constraints, bounds=bounds)

# Print optimized portfolio weights
print(result.x)
