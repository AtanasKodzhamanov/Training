from scipy.stats import norm
import numpy as np
# Option pricing is the process of determining the fair value of an option, which is a contract that gives the buyer the right, but not the obligation, to buy or sell an underlying asset at a predetermined price(strike price) on or before a certain date(expiration date). The value of an option depends on several factors, including the price of the underlying asset, the strike price, the time to expiration, the volatility of the underlying asset, and the risk-free interest rate. Mathematical models such as Black-Scholes or binomial pricing models can be used to estimate the fair value of an option based on these factors. The Black-Scholes model is a widely used option pricing model that was introduced in 1973 by Fischer Black and Myron Scholes. The model assumes that the underlying asset follows a log-normal distribution and that the price of the option can be determined by solving a partial differential equation. The model takes into account the price of the underlying asset, the strike price, the time to expiration, the volatility of the underlying asset, and the risk-free interest rate. The binomial pricing model is another option pricing model that was introduced by Cox, Ross, and Rubinstein in 1979. The model assumes that the price of the underlying asset can either go up or down over a certain period of time, and that the price of the option can be determined by calculating the expected value of the option at each time step. The model takes into account the price of the underlying asset, the strike price, the time to expiration, the volatility of the underlying asset, and the risk-free interest rate. Here are some examples of option pricing using these models in Python:

# Black-Scholes Model


def black_scholes(S, K, T, r, sigma, option_type):
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


# Define parameters
S = 100  # stock price
K = 110  # strike price
T = 1.0  # time to expiration
r = 0.05  # risk-free interest rate
sigma = 0.2  # volatility

# Calculate call and put option prices
call_price = black_scholes(S, K, T, r, sigma, 'call')
put_price = black_scholes(S, K, T, r, sigma, 'put')

# Print results
print(f"Black-Scholes call option price: {call_price:.2f}")
print(f"Black-Scholes put option price: {put_price:.2f}")

# In this example, we calculate the fair value of a call and put option using the Black-Scholes model. We define the stock price, strike price, time to expiration, risk-free interest rate, and volatility, and use the black_scholes function to calculate the call and put option prices. We then print the results.

# Binomial Pricing Model


def binomial_pricing(S, K, T, r, sigma, N, option_type):
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    S_paths = np.zeros((N+1, N+1))
    V_paths = np.zeros((N+1, N+1))
    for i in range(N+1):
        for j in range(i+1):
            S_paths[j, i] = S * u**(i-j) * d**j
            if option_type == 'call':
                V_paths[j, i] = max(S_paths[j, i] - K, 0)
            elif option_type == 'put':
                V_paths[j, i] = max(K - S_paths[j, i], 0)
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            V_paths[j, i] = np.exp(-r * dt) * \
                (p * V_paths[j, i+1] + (1-p) * V_paths[j+1, i+1])
    return V_paths[0, 0]


# Define parameters
S = 100  # stock price
K = 110  # strike price
T = 1.0  # time to expiration
r = 0.05  # risk-free interest rate
sigma = 0.2  # volatility
N = 100  # number of time steps

# Calculate call and put option prices
call_price = binomial_pricing(S, K, T, r, sigma, N, 'call')
put_price = binomial_pricing(S, K, T, r, sigma, N, 'put')

# Print results
print(f"Binomial pricing call option price: {call_price:.2f}")
print(f"Binomial pricing put option price: {put_price:.2f}")
