import numpy as np


def bond_price(face_value, coupon_rate, time_to_maturity, yield_to_maturity):
    c = face_value * coupon_rate
    n = time_to_maturity * 2
    r = yield_to_maturity / 2
    coupon_payments = [c] * int(n)
    coupon_payments[-1] += face_value
    discount_factors = [(1 + r) ** (-i) for i in range(1, int(n) + 1)]
    bond_price = np.dot(coupon_payments, discount_factors)
    return bond_price


def bond_yield(face_value, coupon_rate, time_to_maturity, bond_price):
    coupon_payments = [face_value * coupon_rate] * int(time_to_maturity * 2)
    coupon_payments[-1] += face_value
    periods = np.arange(1, int(time_to_maturity * 2) + 1)

    def ytm_func(y): return np.dot(coupon_payments,
                                   (1 + y / 2) ** (-periods)) - bond_price
    ytm = scipy.optimize.newton(ytm_func, x0=0.05)
    return ytm


# Example usage:
face_value = 1000
coupon_rate = 0.05
time_to_maturity = 5
yield_to_maturity = 0.06
bond_price = bond_price(face_value, coupon_rate,
                        time_to_maturity, yield_to_maturity)
print("Bond price:", bond_price)

bond_yield = bond_yield(face_value, coupon_rate, time_to_maturity, bond_price)
print("Bond yield:", bond_yield)
This code calculates the price and yield to maturity of a bond using the formula for present value of a bond and Newton's method for finding the yield to maturity.
