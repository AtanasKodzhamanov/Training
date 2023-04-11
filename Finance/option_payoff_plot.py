import numpy as np
import matplotlib.pyplot as plt


def call_payoff(S, K, premium):
    return np.maximum(S - K, 0) - premium


def put_payoff(S, K, premium):
    return np.maximum(K - S, 0) - premium


S = np.arange(50, 150)
K = 100
premium = 5
call_payoff = call_payoff(S, K, premium)
put_payoff = put_payoff(S, K, premium)
plt.plot(S, call_payoff, label="Call option")
plt.plot(S, put_payoff, label="Put option")
plt.legend()
plt.xlabel("Stock price")
plt.ylabel("Option payoff")
plt.show()
