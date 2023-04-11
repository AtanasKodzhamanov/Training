

import numpy as np
import pandas as pd
The Capital Asset Pricing Model (CAPM) is a financial theory that describes the relationship between risk and expected return of an asset. According to the CAPM, the expected return on an asset is equal to the risk-free rate plus a risk premium that is proportional to the asset's beta, which measures its sensitivity to market movements. The formula for the CAPM is :

Expected return = Risk-free rate + Beta x(Market risk premium)

Here are some examples of using Python to work with the CAPM:

Calculating beta:
python
Copy code


def calc_beta(stock_returns, market_returns):
    beta = np.cov(stock_returns, market_returns)[0][1] / np.var(market_returns)
    return beta


# Example usage:
df = pd.read_csv('stock_data.csv')
stock_returns = df['stock_returns']
market_returns = df['market_returns']
beta = calc_beta(stock_returns, market_returns)
print('Beta:', beta)
This code calculates the beta of a stock using the formula for covariance and variance.

Calculating expected returns:
python
Copy code


def calc_expected_return(risk_free_rate, beta, market_return):
    expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
    return expected_return


# Example usage:
risk_free_rate = 0.02
beta = 1.2
market_return = 0.08
expected_return = calc_expected_return(risk_free_rate, beta, market_return)
print('Expected return:', expected_return)
This code calculates the expected return of a stock using the CAPM formula.

Portfolio optimization using the CAPM:
python
Copy code


def portfolio_optimization(stock_returns, market_returns, risk_free_rate):
    beta = calc_beta(stock_returns, market_returns)
    expected_market_return = np.mean(market_returns)
    expected_stock_return = calc_expected_return(
        risk_free_rate, beta, expected_market_return)
    return expected_stock_return


# Example usage:
df = pd.read_csv('portfolio_data.csv')
stock_returns = df['stock_returns']
market_returns = df['market_returns']
risk_free_rate = 0.02
expected_portfolio_return = portfolio_optimization(
    stock_returns, market_returns, risk_free_rate)
print('Expected portfolio return:', expected_portfolio_return)
This code optimizes a portfolio using the CAPM by calculating the expected return of each stock and weighting them based on their beta values. The resulting expected portfolio return can be used to make investment decisions.
