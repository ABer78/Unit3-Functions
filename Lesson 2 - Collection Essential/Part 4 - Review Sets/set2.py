# Question 1
# 4
# 7000

# Question 2
# 0x9F1aB3c....

# Question 3
def portfolio_value(holdings, prices):
    total = 0.0
    for coin, amount in holdings.items():
        total += amount * prices[coin]
    return round(total, 2)

holdings = {"BTC":0.5, "ETH": 8.2, "SOL": 50}
prices = {"BTC":62400, "ETH": 2480, "SOL": 142}

print(portfolio_value(holdings, prices)) # 58636.0
