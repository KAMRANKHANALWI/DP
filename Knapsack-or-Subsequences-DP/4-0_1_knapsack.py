# -----------------------------------
# RECURSION
# -----------------------------------

def knapsack(idx, capacity, weights, values):

    # only first item left
    if idx == 0:

        # can pick first item
        if weights[0] <= capacity:
            return values[0]

        # cannot pick
        return 0

    # not-pick
    # ignore current item
    not_pick = knapsack(
        idx - 1,
        capacity,
        weights,
        values
    )

    # pick
    # include current item
    pick = float('-inf')

    # can pick only if current item's weight <= capacity
    if weights[idx] <= capacity:

        # gain current value
        # reduce remaining capacity
        pick = values[idx] + knapsack(
            idx - 1,
            capacity - weights[idx],
            weights,
            values
        )

    # take maximum value possible
    return max(pick, not_pick)


weights = [1, 2, 4, 5]
values = [5, 4, 8, 6]

capacity = 5

n = len(weights)

print(knapsack(n - 1, capacity, weights, values))


# -----------------------------------
# MEMOIZATION
# -----------------------------------

def knapsack_memo(idx, capacity, weights, values, dp):

    # only first item left
    if idx == 0:

        # can pick first item
        if weights[0] <= capacity:
            return values[0]

        return 0

    # dp[idx][capacity]
    # means:
    # maximum value achievable
    # using items from index 0 -> idx
    # with bag capacity = capacity

    # already solved
    if dp[idx][capacity] != -1:
        return dp[idx][capacity]

    # not-pick
    not_pick = knapsack_memo(
        idx - 1,
        capacity,
        weights,
        values,
        dp
    )

    # pick
    pick = float('-inf')

    if weights[idx] <= capacity:

        pick = values[idx] + knapsack_memo(
            idx - 1,
            capacity - weights[idx],
            weights,
            values,
            dp
        )

    # store answer for current state
    dp[idx][capacity] = max(pick, not_pick)

    return dp[idx][capacity]


dp = [[-1] * (capacity + 1) for _ in range(n)]

print(knapsack_memo(n - 1, capacity, weights, values, dp))


# -----------------------------------
# TABULATION
# -----------------------------------

def knapsack_tab(weights, values, capacity):

    n = len(weights)

    # dp[idx][cap]
    # means:
    # maximum value achievable
    # using items from index 0 -> idx
    # with bag capacity = cap

    dp = [[0] * (capacity + 1) for _ in range(n)]

    # first row initialization
    # using only first item

    # if capacity can hold first item
    # then value becomes values[0]
    for cap in range(weights[0], capacity + 1):
        dp[0][cap] = values[0]

    # fill remaining table
    for idx in range(1, n):

        for cap in range(capacity + 1):

            # not-pick
            # take answer from previous row
            not_pick = dp[idx - 1][cap]

            # pick
            pick = float('-inf')

            # can pick only if current item fits
            if weights[idx] <= cap:

                # gain current value
                # reduce remaining capacity
                pick = values[idx] + dp[idx - 1][cap - weights[idx]]

            # store maximum value possible
            dp[idx][cap] = max(pick, not_pick)

    return dp[n - 1][capacity]


print(knapsack_tab(weights, values, capacity))


# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def knapsack_space_optimized(weights, values, capacity):

    n = len(weights)

    # prev[cap]
    # means:
    # maximum value achievable
    # using previous row items
    # with capacity = cap

    prev = [0] * (capacity + 1)

    # first item initialization
    for cap in range(weights[0], capacity + 1):
        prev[cap] = values[0]

    # fill remaining rows
    for idx in range(1, n):

        curr = [0] * (capacity + 1)

        for cap in range(capacity + 1):

            # not-pick
            not_pick = prev[cap]

            # pick
            pick = float('-inf')

            if weights[idx] <= cap:

                # gain current value
                # reduce remaining capacity
                pick = values[idx] + prev[cap - weights[idx]]

            # store best value
            curr[cap] = max(pick, not_pick)

        prev = curr

    return prev[capacity]


print(knapsack_space_optimized(weights, values, capacity))