class FinancialInstrument:
    def __init__(self, symbol, price, quantity):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def calculate_value(self):
        return self.price * self.quantity


class Stock(FinancialInstrument):
    def __init__(self, symbol, price, quantity, dividend_yield):
        super().init(symbol, price, quantity)
        self.dividend_yield = dividend_yield

    def calculate_dividend(self):
        return self.calculate_value() * self.dividend_yield

