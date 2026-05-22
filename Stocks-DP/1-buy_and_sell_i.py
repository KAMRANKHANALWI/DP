# =========================================================
# BEST TIME TO BUY AND SELL STOCK
# ONE TRANSACTION
# =========================================================


def max_profit(prices):
    n = len(prices)
    min_price = prices[0]
    max_profit = 0
    for i in range(1, n):
        profit = prices[i] - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, prices[i])
    
    return max_profit
    

prices = [7,1,5,3,6,4]
print(max_profit(prices))