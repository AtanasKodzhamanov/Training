import numpy as np

S = 100  # stock price
K = 105  # strike price
T = 1    # time to expiration (in years)
r = 0.05  # risk-free interest rate
sigma = 0.2  # volatility
num_simulations = 1000
num_steps = 252
dt = T / num_steps

sims = np.zeros((num_simulations, num_steps + 1))
sims[:, 0] = S
for i in range(num_simulations):
    for j in range(1, num_steps + 1):
        eps = np.random.normal()
        sims[i, j] = sims[i, j - 1] * \
            np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * eps)

call_payoffs = np.maximum(sims[:, -1] - K, 0)
put_payoffs = np.maximum(K - sims[:, -1], 0)

call_price = np.mean(np.exp(-r * T) * call_payoffs)
put_price = np.mean(np.exp(-r * T) * put_payoffs)

print("Call price:", call_price)
print("Put price:", put_price)
