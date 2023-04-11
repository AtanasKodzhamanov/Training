import pandas as pd


def calculate_max_drawdown(symbols, start_date, end_date):
    # Load the historical price data for each stock
    prices = pd.DataFrame()
    for symbol in symbols:
        df = pd.read_csv(
            f"{symbol}.csv", index_col="timestamp", parse_dates=["timestamp"])
        prices[symbol] = df.loc[start_date:end_date]["close"]

    # Calculate the returns and maximum drawdown
    returns = prices.pct_change().dropna()
    cum_returns = (1 + returns).cumprod()
    max_drawdown = (cum_returns.cummax() - cum_returns) / cum_returns.cummax()
    max_drawdown = max_drawdown.max()

    return max_drawdown
