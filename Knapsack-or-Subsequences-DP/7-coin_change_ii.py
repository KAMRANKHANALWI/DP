# -----------------------------------
# RECURSION
# -----------------------------------

def coin_change_2(idx, target, coins):

    # target formed successfully
    # found one valid way
    if target == 0:
        return 1

    # only first coin left
    if idx == 0:

        # if target divisible
        # one valid way exists
        if target % coins[0] == 0:
            return 1

        return 0

    # not-pick
    # move to previous coin
    not_pick = coin_change_2(
        idx - 1,
        target,
        coins
    )

    # pick
    # stay at same index
    # because coin reusable infinitely
    pick = 0

    if coins[idx] <= target:

        pick = coin_change_2(
            idx,
            target - coins[idx],
            coins
        )

    # total ways
    return pick + not_pick


coins = [1, 2, 5]
target = 5

n = len(coins)

print(coin_change_2(n - 1, target, coins))


# -----------------------------------
# MEMOIZATION
# -----------------------------------

def coin_change_2_memo(idx, target, coins, dp):

    # target formed successfully
    if target == 0:
        return 1

    # only first coin left
    if idx == 0:

        if target % coins[0] == 0:
            return 1

        return 0

    # dp[idx][target]
    # means:
    # number of ways
    # to form target
    # using coins from 0 -> idx

    # already solved
    if dp[idx][target] != -1:
        return dp[idx][target]

    # not-pick
    not_pick = coin_change_2_memo(
        idx - 1,
        target,
        coins,
        dp
    )

    # pick
    pick = 0

    if coins[idx] <= target:

        # stay at same index
        # because unlimited reuse allowed
        pick = coin_change_2_memo(
            idx,
            target - coins[idx],
            coins,
            dp
        )

    # store total ways
    dp[idx][target] = pick + not_pick

    return dp[idx][target]


dp = [[-1] * (target + 1) for _ in range(n)]

print(coin_change_2_memo(n - 1, target, coins, dp))


# -----------------------------------
# TABULATION
# -----------------------------------

def coin_change_2_tab(coins, target):

    n = len(coins)

    # dp[idx][t]
    # means:
    # number of ways
    # to form target t
    # using coins from 0 -> idx

    dp = [[0] * (target + 1) for _ in range(n)]

    # first row initialization
    # using only first coin
    for t in range(target + 1):

        # if divisible
        # one valid way exists
        if t % coins[0] == 0:
            dp[0][t] = 1

    # fill remaining table
    for idx in range(1, n):

        for t in range(target + 1):

            # not-pick
            not_pick = dp[idx - 1][t]

            # pick
            pick = 0

            if coins[idx] <= t:

                # stay at same row
                # because coin reusable infinitely
                pick = dp[idx][t - coins[idx]]

            # total ways
            dp[idx][t] = pick + not_pick

    return dp[n - 1][target]


print(coin_change_2_tab(coins, target))


# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def coin_change_2_space_optimized(coins, target):

    n = len(coins)

    # prev[t]
    # means:
    # number of ways
    # to form target t
    # using previous row coins

    prev = [0] * (target + 1)

    # first row initialization
    for t in range(target + 1):

        if t % coins[0] == 0:
            prev[t] = 1

    # fill remaining rows
    for idx in range(1, n):

        curr = [0] * (target + 1)

        for t in range(target + 1):

            # not-pick
            not_pick = prev[t]

            # pick
            pick = 0

            if coins[idx] <= t:

                # stay at same row
                # because unlimited reuse allowed
                pick = curr[t - coins[idx]]

            curr[t] = pick + not_pick

        prev = curr

    return prev[target]


print(coin_change_2_space_optimized(coins, target))