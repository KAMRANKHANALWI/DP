# -----------------------------------
# RECURSION
# -----------------------------------

def subset_sum(arr, idx, target):

    # target became 0
    # means we successfully formed the target
    if target == 0:
        return True

    # only first element left
    # can we form target using only arr[0] ?
    if idx == 0:
        return arr[0] == target

    # not-pick
    # ignore current element
    # move to previous index
    not_pick = subset_sum(arr, idx - 1, target)

    # pick
    # take current element
    # reduce target
    pick = False

    if target >= arr[idx]:
        pick = subset_sum(arr, idx - 1, target - arr[idx])

    # if either pick or not-pick works
    # answer becomes True
    return pick or not_pick


arr = [1, 2, 3, 4]
target = 4

n = len(arr)

print(subset_sum(arr, n - 1, target))


# -----------------------------------
# MEMOIZATION
# -----------------------------------

def subset_sum_memo(arr, idx, target, dp):

    # target became 0
    # means target successfully formed
    if target == 0:
        return True

    # only first element left
    # can arr[0] alone form target ?
    if idx == 0:
        return arr[0] == target

    # dp[idx][target]
    # means:
    # can I form target
    # using elements from 0 -> idx

    # if already solved
    # reuse answer
    if dp[idx][target] != -1:
        return dp[idx][target]

    # not-pick
    # ignore current element
    not_pick = subset_sum_memo(arr, idx - 1, target, dp)

    # pick
    # include current element
    pick = False

    if target >= arr[idx]:
        pick = subset_sum_memo(arr, idx - 1, target - arr[idx], dp)

    # store final answer for current state
    dp[idx][target] = not_pick or pick

    return dp[idx][target]


dp = [[-1] * (target + 1) for _ in range(n)]

print(subset_sum_memo(arr, n - 1, target, dp))


# -----------------------------------
# TABULATION
# -----------------------------------

def subset_sum_tab(arr, target):

    n = len(arr)

    # dp[idx][t]
    # means:
    # can I form target t
    # using elements from index 0 -> idx

    dp = [[False] * (target + 1) for _ in range(n)]

    # target 0 is always possible
    # choose empty subset
    for idx in range(n):
        dp[idx][0] = True

    # first row initialization
    # using only arr[0]
    # we can form only target arr[0]
    if arr[0] <= target:
        dp[0][arr[0]] = True

    # fill remaining table
    for idx in range(1, n):

        for t in range(1, target + 1):

            # not-pick
            # take answer from previous row
            not_pick = dp[idx - 1][t]

            # pick
            pick = False

            # can pick only if current element <= target
            if arr[idx] <= t:

                # remaining target after picking arr[idx]
                pick = dp[idx - 1][t - arr[idx]]

            # if either works -> True
            dp[idx][t] = pick or not_pick

    return dp[n - 1][target]


print(subset_sum_tab(arr, target))


# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def subset_sum_space_optimized(arr, target):

    n = len(arr)

    # prev[t]
    # means:
    # can I form target t
    # using previous row elements

    prev = [False] * (target + 1)

    # target 0 always possible
    prev[0] = True

    # first element
    if arr[0] <= target:
        prev[arr[0]] = True

    for idx in range(1, n):

        curr = [False] * (target + 1)

        # target 0 always possible
        curr[0] = True

        for t in range(1, target + 1):

            # not-pick
            not_pick = prev[t]

            # pick
            pick = False

            if arr[idx] <= t:

                # remaining target after picking current element
                pick = prev[t - arr[idx]]

            curr[t] = pick or not_pick

        prev = curr

    return prev[target]


print(subset_sum_space_optimized(arr, target))