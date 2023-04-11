# Write a program that calculates the simple moving average (SMA) of a list of stock prices. The function should take the list of prices and the window size as input and return a list of moving averages.

def calculate_sma(prices, window):
    sma = []
    for i in range(window - 1, len(prices)):
        sma.append(sum(prices[i - window + 1:i + 1]) / window)
    return sma
