import pandas as pd


def calculate_covariance_matrix(symbols, start_date, end_date):
    # Load the historical price data for each stock
    prices = pd.DataFrame()
    for symbol in symbols:
        df = pd.read_csv(
            f"{symbol}.csv", index_col="timestamp", parse_dates=["timestamp"])
        prices[symbol] = df.loc[start_date:end_date]["close"]

    # Calculate the returns and covariance matrix
    returns = prices.pct_change().dropna()
    cov = returns.cov()

    return cov
