# ---------------------------------------------------------
# LOGIC
# ---------------------------------------------------------

# positive subset  -> P
# negative subset  -> N

# P + N = total_sum
# P - N = target

# adding both:

# 2P = total_sum + target

# therefore:

# P = (total_sum + target) // 2

# so problem becomes:

# COUNT SUBSETS WITH SUM = P


# -----------------------------------
# RECURSION
# -----------------------------------

def count_subsets(arr, idx, target):

    # target formed successfully
    # found one valid subset
    if target == 0:
        return 1

    # only first element left
    if idx == 0:

        if arr[0] == target:
            return 1

        return 0

    # not-pick
    # ignore current element
    not_pick = count_subsets(
        arr,
        idx - 1,
        target
    )

    # pick
    pick = 0

    if arr[idx] <= target:

        # reduce remaining target
        pick = count_subsets(
            arr,
            idx - 1,
            target - arr[idx]
        )

    # total ways
    return pick + not_pick


def target_sum(arr, target):

    total_sum = sum(arr)

    # impossible case
    if (total_sum + target) % 2 != 0:
        return 0

    subset_target = (total_sum + target) // 2

    n = len(arr)

    return count_subsets(
        arr,
        n - 1,
        subset_target
    )


arr = [1, 1, 1, 1, 1]
target = 3

print(target_sum(arr, target))


# -----------------------------------
# MEMOIZATION
# -----------------------------------

def count_subsets_memo(arr, idx, target, dp):

    # target formed
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
    # forming target
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

    # store answer
    dp[idx][target] = pick + not_pick

    return dp[idx][target]


def target_sum_memo(arr, target):

    total_sum = sum(arr)

    if (total_sum + target) % 2 != 0:
        return 0

    subset_target = (total_sum + target) // 2

    n = len(arr)

    dp = [[-1] * (subset_target + 1) for _ in range(n)]

    return count_subsets_memo(
        arr,
        n - 1,
        subset_target,
        dp
    )


print(target_sum_memo(arr, target))


# -----------------------------------
# TABULATION
# -----------------------------------

def target_sum_tab(arr, target):

    total_sum = sum(arr)

    # impossible case
    if (total_sum + target) % 2 != 0:
        return 0

    subset_target = (total_sum + target) // 2

    n = len(arr)

    # dp[idx][t]
    # means:
    # number of subsets
    # forming target t
    # using elements from 0 -> idx

    dp = [[0] * (subset_target + 1) for _ in range(n)]

    # target 0 always possible
    # choose empty subset
    for idx in range(n):
        dp[idx][0] = 1

    # first element initialization
    if arr[0] <= subset_target:
        dp[0][arr[0]] = 1

    # fill remaining table
    for idx in range(1, n):

        for t in range(subset_target + 1):

            # not-pick
            not_pick = dp[idx - 1][t]

            # pick
            pick = 0

            if arr[idx] <= t:

                pick = dp[idx - 1][t - arr[idx]]

            # total ways
            dp[idx][t] = pick + not_pick

    return dp[n - 1][subset_target]


print(target_sum_tab(arr, target))


# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def target_sum_space_optimized(arr, target):

    total_sum = sum(arr)

    if (total_sum + target) % 2 != 0:
        return 0

    subset_target = (total_sum + target) // 2

    n = len(arr)

    # prev[t]
    # means:
    # number of subsets
    # forming target t
    # using previous row elements

    prev = [0] * (subset_target + 1)

    # empty subset
    prev[0] = 1

    # first element
    if arr[0] <= subset_target:
        prev[arr[0]] = 1

    for idx in range(1, n):

        curr = [0] * (subset_target + 1)

        curr[0] = 1

        for t in range(subset_target + 1):

            # not-pick
            not_pick = prev[t]

            # pick
            pick = 0

            if arr[idx] <= t:

                pick = prev[t - arr[idx]]

            curr[t] = pick + not_pick

        prev = curr

    return prev[subset_target]


print(target_sum_space_optimized(arr, target))