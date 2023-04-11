# The cash flows are represented as a list of tuples, with each tuple containing the cash flow amount and the time period.

def calculate_npv(investment,cashflows, rate):
    npv = 0
    for cashflow in cashflows:
        amount, time = cashflow
        discounted_cf = amount / ((1 + rate) ** time)
        npv += discounted_cf
        print("Discounted cash flow in year " + str(time) + " : " + str(round(discounted_cf,2)))

    npv-=investment
    print("Net present value: " + str(round(npv,2)))

calculate_npv(400,[(200, 1), (150, 2), (150, 3)], 0.2)