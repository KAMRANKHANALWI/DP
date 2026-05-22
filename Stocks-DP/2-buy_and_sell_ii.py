# =========================================================
# BUY AND SELL STOCK II
# UNLIMITED TRANSACTIONS
# =========================================================


# -----------------------------------
# RECURSION
# -----------------------------------


def stock(idx, buy, prices, n):

    # no days left
    if idx == n:
        return 0

    # -----------------------------------
    # CAN BUY
    # -----------------------------------
    if buy:

        # buy stock today
        # money spent -> negative
        take = -prices[idx] + stock(idx + 1, 0, prices, n)

        # skip buying
        not_take = stock(idx + 1, 1, prices, n)

        # maximize profit
        return max(take, not_take)

    # -----------------------------------
    # MUST SELL
    # -----------------------------------
    else:

        # sell stock today
        sell = prices[idx] + stock(idx + 1, 1, prices, n)

        # hold stock
        not_sell = stock(idx + 1, 0, prices, n)

        # maximize profit
        return max(sell, not_sell)


prices = [7, 1, 5, 3, 6, 4]

n = len(prices)

print(stock(0, 1, prices, n))


# -----------------------------------
# MEMOIZATION
# -----------------------------------


def stock_memo(idx, buy, prices, n, dp):

    # no days left
    if idx == n:
        return 0

    # dp[idx][buy]
    # means:
    # maximum profit
    # starting from idx
    # in current buy state

    # already solved
    if dp[idx][buy] != -1:
        return dp[idx][buy]

    # can buy
    if buy:

        take = -prices[idx] + stock_memo(idx + 1, 0, prices, n, dp)

        not_take = stock_memo(idx + 1, 1, prices, n, dp)

        dp[idx][buy] = max(take, not_take)

    # must sell
    else:

        sell = prices[idx] + stock_memo(idx + 1, 1, prices, n, dp)

        not_sell = stock_memo(idx + 1, 0, prices, n, dp)

        dp[idx][buy] = max(sell, not_sell)

    return dp[idx][buy]


dp = [[-1] * 2 for _ in range(n)]

print(stock_memo(0, 1, prices, n, dp))


# -----------------------------------
# TABULATION
# -----------------------------------


def stock_tab(prices):

    n = len(prices)

    # dp[idx][buy]
    # means:
    # maximum profit
    # from idx onward
    # in current buy state

    dp = [[0] * 2 for _ in range(n + 1)]

    # base case already 0
    # dp[n][0] = dp[n][1] = 0

    # fill backwards
    for idx in range(n - 1, -1, -1):

        for buy in range(2):

            # can buy
            if buy:

                take = -prices[idx] + dp[idx + 1][0]

                not_take = dp[idx + 1][1]

                dp[idx][buy] = max(take, not_take)

            # must sell
            else:

                sell = prices[idx] + dp[idx + 1][1]

                not_sell = dp[idx + 1][0]

                dp[idx][buy] = max(sell, not_sell)

    return dp[0][1]


print(stock_tab(prices))

# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------


def stock_space_optimized(prices):

    n = len(prices)

    # next day's states
    ahead = [0] * 2

    # fill backwards
    for idx in range(n - 1, -1, -1):

        curr = [0] * 2

        # can buy
        curr[1] = max(-prices[idx] + ahead[0], ahead[1])

        # must sell
        curr[0] = max(prices[idx] + ahead[1], ahead[0])

        ahead = curr

    return ahead[1]


print(stock_space_optimized(prices))
