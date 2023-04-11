# Monte Carlo simulation is a technique used to model the probability distribution
# of an asset's future price movements by generating random price paths and
# estimating their expected value. The technique involves creating a large
# number of simulations of the asset's future price movements, with each
# simulation representing a possible outcome of the asset's price path
# based on its current value, volatility, and other factors.
# The simulations are run using random numbers and statistical
# models to generate a range of possible outcomes, which can be used
# to estimate the expected value of the asset and assess its risk and uncertainty.

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
S = 100  # initial stock price
r = 0.05  # risk-free rate
sigma = 0.2  # volatility
T = 1.0  # time horizon
N = 252  # number of time steps
M = 10000  # number of simulations

# Calculate drift and diffusion
dt = T / N
mu = r - 0.5 * sigma**2
z = np.random.normal(size=(M, N))

# Generate price paths
S_paths = np.zeros((M, N+1))
S_paths[:, 0] = S
for i in range(1, N+1):
    S_paths[:, i] = S_paths[:, i-1] * \
        np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z[:, i-1])

# Plot price paths
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(S_paths.T)
ax.set_xlabel('Time')
ax.set_ylabel('Price')
plt.show()

# Calculate statistics
S_mean = np.mean(S_paths[:, -1])
S_std = np.std(S_paths[:, -1])
S_ci = np.percentile(S_paths[:, -1], [2.5, 97.5])

# Print results
print(f"Expected price at time T: {S_mean:.2f}")
print(f"Standard deviation of price at time T: {S_std:.2f}")
print(
    f"95% confidence interval of price at time T: [{S_ci[0]:.2f}, {S_ci[1]:.2f}]")
