import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data
data = pd.read_csv('asset_returns.csv', index_col=0)
weights = np.array([0.5, 0.5])
cov_matrix = data.cov()

# Define portfolio return function


def portfolio_return(weights, expected_returns):
    return np.dot(weights.T, expected_returns)

# Define portfolio risk function


def portfolio_risk(weights, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

# Define Monte Carlo simulation function


def monte_carlo_simulations(data, weights, cov_matrix, n_simulations=10000):
    portfolio_returns = []
    for i in range(n_simulations):
        sim_data = np.random.multivariate_normal(data.mean(), cov_matrix)
        portfolio_return_sim = portfolio_return(weights, sim_data)
        portfolio_returns.append(portfolio_return_sim)
    portfolio_returns = np.array(portfolio_returns)
    portfolio_returns.sort()
    return portfolio_returns


# Calculate portfolio VaR using Monte Carlo simulation
portfolio_returns = monte_carlo_simulations(data, weights, cov_matrix)
portfolio_var = -np.percentile(portfolio_returns, 5)

# Plot returns distribution and VaR
plt.hist(portfolio_returns, bins=50)
plt.axvline(x=-portfolio_var, color='r', linestyle='--')
plt.xlabel('Portfolio Returns')
plt.ylabel('Frequency')
plt.title('Portfolio Returns Distribution')
plt.show()

# Print results
print(f"Portfolio VaR (95% confidence interval): {portfolio_var:.2%}")
