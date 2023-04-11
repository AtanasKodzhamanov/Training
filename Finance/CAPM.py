

import numpy as np
import pandas as pd
# CAPM, the expected return on an asset is equal to the risk-free rate plus a risk premium that is proportional to the asset's beta, which measures its sensitivity to market movements. 

# Expected return = Risk-free rate + Beta x(Market risk premium)

def calc_beta(stock_returns, market_returns):
    beta = np.cov(stock_returns, market_returns)[0][1] / np.var(market_returns)
    return beta

# Example usage:
df = pd.read_csv('stock_data.csv')
stock_returns = df['stock_returns']
market_returns = df['market_returns']
beta = calc_beta(stock_returns, market_returns)
print('Beta:', beta)

def calc_expected_return(risk_free_rate, beta, market_return):
    expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
    return expected_return

# Example usage:
risk_free_rate = 0.02
beta = 1.2
market_return = 0.08
expected_return = calc_expected_return(risk_free_rate, beta, market_return)
print('Expected return:', expected_return)

def portfolio_optimization(stock_returns, market_returns, risk_free_rate):
    beta = calc_beta(stock_returns, market_returns)
    expected_market_return = np.mean(market_returns)
    expected_stock_return = calc_expected_return(risk_free_rate, beta, expected_market_return)
    return expected_stock_return

# Example usage:
df = pd.read_csv('portfolio_data.csv')
stock_returns = df['stock_returns']
market_returns = df['market_returns']
risk_free_rate = 0.02
expected_portfolio_return = portfolio_optimization(stock_returns, market_returns, risk_free_rate)
print('Expected portfolio return:', expected_portfolio_return)
