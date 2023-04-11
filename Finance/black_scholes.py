from scipy.stats import norm
import numpy as np

# The "Greeks"

# Delta: Delta measures the sensitivity of an option's price to changes in the price of the underlying asset. For call options, delta is a number between 0 and 1, with higher numbers indicating a stronger correlation between the option's price and the underlying asset's price. For put options, delta is a number between - 1 and 0.

# Gamma: Gamma measures the rate at which delta changes as the price of the underlying asset changes. 

# Theta: Theta measures the rate at which an option's value declines over time as it gets closer to expiration. 

# Vega: Vega measures the sensitivity of an option's price to changes in the volatility of the underlying asset. 

# Rho: Rho measures the sensitivity of an option's price to changes in interest rates. 

# The greeks can be derived from the partial derivatives of the Black-Scholes formula.

def black_scholes_call(S, K, T, r, sigma):
    
    d1 = (np.log(S/K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # expected value of stock price at expiration, the product of the current stock price (S) and the probability that the stock price will be above the strike price at expiration (N(d1))
    EVatExp = S * norm.cdf(d1)    
    
    PVofStrikePrice = K * np.exp(-r * T) * norm.cdf(d2)
    
    call_price = EVatExp  - PVofStrikePrice
    return call_price

S = 100  # stock price
K = 105  # strike price
T = 1    # time to expiration (in years)
r = 0.05  # risk-free interest rate
sigma = 0.2  # volatility (std of the stocks price)
call_price = black_scholes_call(S, K, T, r, sigma)
print("Call price:", call_price)
