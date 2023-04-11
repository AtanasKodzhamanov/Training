def calculate_irr(cashflows):
    # Define the IRR function as the root of the NPV equation
    def npv_irr(rate):
        npv = 0
        for cashflow in cashflows:
            amount, time = cashflow
            npv += amount / (1 + rate) ** time
        return npv

    # Use the bisection method to find the root of the NPV equation
    epsilon = 0.0001
    a, b = -1.0, 1.0
    while (b - a) > epsilon:
        c = (a + b) / 2.0
        if npv_irr(a) * npv_irr(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0
