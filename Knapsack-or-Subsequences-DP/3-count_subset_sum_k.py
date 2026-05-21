# -----------------------------------
# RECURSION
# -----------------------------------

def count_subsets(arr, idx, target):

    # target formed successfully
    # found one valid subset
    if target == 0:
        return 1

    # only first element left
    # can arr[0] alone form target ?
    if idx == 0:

        if arr[0] == target:
            return 1

        return 0

    # not-pick
    # ignore current element
    not_pick = count_subsets(arr, idx - 1, target)

    # pick
    # include current element
    pick = 0

    if arr[idx] <= target:

        # reduce remaining target
        pick = count_subsets(
            arr,
            idx - 1,
            target - arr[idx]
        )

    # total ways
    # = pick ways + not-pick ways
    return pick + not_pick


arr = [1, 2, 2, 3]
target = 3

n = len(arr)

print(count_subsets(arr, n - 1, target))


# -----------------------------------
# MEMOIZATION
# -----------------------------------

def count_subsets_memo(arr, idx, target, dp):

    # target formed successfully
    if target == 0:
        return 1

    # only first element left
    if idx == 0:

        if arr[0] == target:
            return 1

        return 0

    # dp[idx][target]
    # means:
    # number of subsets
    # that can form target
    # using elements from 0 -> idx

    # already solved
    if dp[idx][target] != -1:
        return dp[idx][target]

    # not-pick
    not_pick = count_subsets_memo(
        arr,
        idx - 1,
        target,
        dp
    )

    # pick
    pick = 0

    if arr[idx] <= target:

        pick = count_subsets_memo(
            arr,
            idx - 1,
            target - arr[idx],
            dp
        )

    # store total ways
    dp[idx][target] = pick + not_pick

    return dp[idx][target]


dp = [[-1] * (target + 1) for _ in range(n)]

print(count_subsets_memo(arr, n - 1, target, dp))


# -----------------------------------
# TABULATION
# -----------------------------------

def count_subsets_tab(arr, target):

    n = len(arr)

    # dp[idx][t]
    # means:
    # number of subsets
    # that can form target t
    # using elements from 0 -> idx

    dp = [[0] * (target + 1) for _ in range(n)]

    # target 0 can always be formed
    # by choosing empty subset
    for idx in range(n):
        dp[idx][0] = 1

    # first element initialization
    if arr[0] <= target:
        dp[0][arr[0]] = 1

    # fill remaining table
    for idx in range(1, n):

        for t in range(target + 1):

            # not-pick
            not_pick = dp[idx - 1][t]

            # pick
            pick = 0

            if arr[idx] <= t:

                pick = dp[idx - 1][t - arr[idx]]

            # total ways
            dp[idx][t] = pick + not_pick

    return dp[n - 1][target]


print(count_subsets_tab(arr, target))


# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def count_subsets_space_optimized(arr, target):

    n = len(arr)

    # prev[t]
    # means:
    # number of subsets
    # forming target t
    # using previous row elements

    prev = [0] * (target + 1)

    # target 0 always possible
    prev[0] = 1

    # first element
    if arr[0] <= target:
        prev[arr[0]] = 1

    for idx in range(1, n):

        curr = [0] * (target + 1)

        # empty subset
        curr[0] = 1

        for t in range(target + 1):

            # not-pick
            not_pick = prev[t]

            # pick
            pick = 0

            if arr[idx] <= t:

                pick = prev[t - arr[idx]]

            curr[t] = pick + not_pick

        prev = curr

    return prev[target]


print(count_subsets_space_optimized(arr, target))