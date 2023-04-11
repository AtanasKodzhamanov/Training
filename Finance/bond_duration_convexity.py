import numpy as np
# Duration measures the sensitivity of a bond's price to changes in interest rates. It takes into account the time to maturity of the bond, the coupon rate, and the current level of interest rates. A higher duration indicates that a bond's price is more sensitive to changes in interest rates. For example, if interest rates rise, the price of a bond with a longer duration will fall more than the price of a bond with a shorter duration.

# Modified duration = (1 / (1 + y)) x [(1 - (1 + y)^(-n)) / y] + (n / (1 + y)^n)

# y is the yield to maturity of the bond
# n is the time to maturity of the bond in years
# c is the periodic coupon payment (annual coupon rate x face value / coupon payment frequency)
# r is the periodic yield to maturity (annual yield to maturity / coupon payment frequency)
# present_values are the present values of each coupon payment

# Assume semi-annual coupon payments


def bond_duration(face_value, coupon_rate, time_to_maturity, yield_to_maturity):
    c = face_value * coupon_rate
    n = time_to_maturity * 2
    r = yield_to_maturity / 2
    coupon_payments = [c] * int(n)
    coupon_payments[-1] += face_value
    discount_factors = [(1 + r) ** (-i) for i in range(1, int(n) + 1)]
    present_values = [d * c for d, c in zip(discount_factors, coupon_payments)]
    bond_price = np.dot(coupon_payments, discount_factors)
    duration = np.dot(np.arange(1, int(n) + 1), present_values) / bond_price
    return duration

# Convexity is a measure of the curvature of the relationship between bond prices and interest rates. It provides a more refined measure of interest rate risk than duration alone, taking into account the non-linear relationship between bond prices and interest rates. A higher convexity indicates that a bond's price is more sensitive to changes in interest rates, particularly when interest rates are far from the bond's coupon rate. For example, a bond with high convexity will have a larger increase in price when interest rates fall than the decrease in price when interest rates rise.


def bond_convexity(face_value, coupon_rate, time_to_maturity, yield_to_maturity):
    c = face_value * coupon_rate
    n = time_to_maturity * 2
    r = yield_to_maturity / 2
    coupon_payments = [c] * int(n)
    coupon_payments[-1] += face_value
    discount_factors = [(1 + r) ** (-i) for i in range(1, int(n) + 1)]
    present_values = [d * c for d, c in zip(discount_factors, coupon_payments)]
    bond_price = np.dot(coupon_payments, discount_factors)
    convexity = np.dot(np.power(np.arange(1, int(n) + 1), 2),
                       present_values) / bond_price
    convexity /= (1 + r) ** 2
    return convexity

