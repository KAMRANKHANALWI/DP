# -----------------------------------
# RECURSION
# -----------------------------------

def min_coins(idx, target, coins):

    # only first coin left
    if idx == 0:

        # if target divisible by first coin
        # exact coins can be formed
        if target % coins[0] == 0:
            return target // coins[0]

        # impossible to form target
        return float('inf')

    # not-pick
    # move to previous coin
    not_pick = min_coins(
        idx - 1,
        target,
        coins
    )

    # pick
    # stay at same index
    # because coins can be reused
    pick = float('inf')

    if coins[idx] <= target:

        pick = 1 + min_coins(
            idx,
            target - coins[idx],
            coins
        )

    # minimum coins needed
    return min(pick, not_pick)


coins = [1, 2, 3]
target = 7

n = len(coins)

ans = min_coins(n - 1, target, coins)

if ans == float('inf'):
    print(-1)
else:
    print(ans)


# -----------------------------------
# MEMOIZATION
# -----------------------------------

def min_coins_memo(idx, target, coins, dp):

    # only first coin left
    if idx == 0:

        if target % coins[0] == 0:
            return target // coins[0]

        return float('inf')

    # dp[idx][target]
    # means:
    # minimum coins needed
    # to form target
    # using coins from 0 -> idx

    # already solved
    if dp[idx][target] != -1:
        return dp[idx][target]

    # not-pick
    not_pick = min_coins_memo(
        idx - 1,
        target,
        coins,
        dp
    )

    # pick
    pick = float('inf')

    if coins[idx] <= target:

        # stay at same index
        # because coin reusable
        pick = 1 + min_coins_memo(
            idx,
            target - coins[idx],
            coins,
            dp
        )

    # store minimum answer
    dp[idx][target] = min(pick, not_pick)

    return dp[idx][target]


dp = [[-1] * (target + 1) for _ in range(n)]

ans = min_coins_memo(n - 1, target, coins, dp)

if ans == float('inf'):
    print(-1)
else:
    print(ans)


# -----------------------------------
# TABULATION
# -----------------------------------

def min_coins_tab(coins, target):

    n = len(coins)

    # dp[idx][t]
    # means:
    # minimum coins needed
    # to form target t
    # using coins from 0 -> idx

    dp = [[0] * (target + 1) for _ in range(n)]

    # first row initialization
    # using only first coin
    for t in range(target + 1):

        # if divisible
        if t % coins[0] == 0:

            dp[0][t] = t // coins[0]

        else:
            dp[0][t] = float('inf')

    # fill remaining table
    for idx in range(1, n):

        for t in range(target + 1):

            # not-pick
            not_pick = dp[idx - 1][t]

            # pick
            pick = float('inf')

            if coins[idx] <= t:

                # stay at same row
                # because unlimited reuse allowed
                pick = 1 + dp[idx][t - coins[idx]]

            # minimum coins needed
            dp[idx][t] = min(pick, not_pick)

    ans = dp[n - 1][target]

    if ans == float('inf'):
        return -1

    return ans


print(min_coins_tab(coins, target))


# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def min_coins_space_optimized(coins, target):

    n = len(coins)

    # prev[t]
    # means:
    # minimum coins needed
    # to form target t
    # using previous row coins

    prev = [0] * (target + 1)

    # first row initialization
    for t in range(target + 1):

        if t % coins[0] == 0:
            prev[t] = t // coins[0]

        else:
            prev[t] = float('inf')

    # fill remaining rows
    for idx in range(1, n):

        curr = [0] * (target + 1)

        for t in range(target + 1):

            # not-pick
            not_pick = prev[t]

            # pick
            pick = float('inf')

            if coins[idx] <= t:

                # stay at same row
                # because coin reusable
                pick = 1 + curr[t - coins[idx]]

            curr[t] = min(pick, not_pick)

        prev = curr

    ans = prev[target]

    if ans == float('inf'):
        return -1

    return ans


print(min_coins_space_optimized(coins, target))