# -----------------------------------
# RECURSION
# -----------------------------------

def lis(idx, prev_idx, arr, n):

    # array exhausted
    if idx == n:
        return 0

    # not-pick
    # ignore current element
    not_pick = lis(
        idx + 1,
        prev_idx,
        arr,
        n
    )

    # pick
    pick = 0

    # can pick if:
    # no previous element selected
    # OR current element > previous selected element
    if (
        prev_idx == -1
        or
        arr[idx] > arr[prev_idx]
    ):

        pick = 1 + lis(
            idx + 1,
            idx,
            arr,
            n
        )

    # maximum LIS length
    return max(pick, not_pick)


arr = [10, 9, 2, 5, 3, 7, 101, 18]

n = len(arr)

print(lis(0, -1, arr, n))


# -----------------------------------
# MEMOIZATION
# -----------------------------------

def lis_memo(idx, prev_idx, arr, n, dp):

    # array exhausted
    if idx == n:
        return 0

    # dp[idx][prev_idx+1]
    # means:
    # LIS length starting from idx
    # with previous selected index = prev_idx

    # +1 shifting used because:
    # prev_idx can be -1

    # already solved
    if dp[idx][prev_idx + 1] != -1:
        return dp[idx][prev_idx + 1]

    # not-pick
    not_pick = lis_memo(
        idx + 1,
        prev_idx,
        arr,
        n,
        dp
    )

    # pick
    pick = 0

    if (
        prev_idx == -1
        or
        arr[idx] > arr[prev_idx]
    ):

        pick = 1 + lis_memo(
            idx + 1,
            idx,
            arr,
            n,
            dp
        )

    # store maximum answer
    dp[idx][prev_idx + 1] = max(
        pick,
        not_pick
    )

    return dp[idx][prev_idx + 1]


dp = [[-1] * (n + 1) for _ in range(n)]

print(lis_memo(0, -1, arr, n, dp))

# -----------------------------------
# TABULATION
# -----------------------------------

def lis_tab(arr):

    n = len(arr)

    # dp[idx][prev+1]
    # means:
    # LIS length starting from idx
    # with previous selected index = prev

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # fill table backwards
    for idx in range(n - 1, -1, -1):

        for prev_idx in range(idx - 1, -2, -1):

            # not-pick
            not_pick = dp[idx + 1][prev_idx + 1]

            # pick
            pick = 0

            if (
                prev_idx == -1
                or
                arr[idx] > arr[prev_idx]
            ):

                pick = 1 + dp[idx + 1][idx + 1]

            # store maximum LIS length
            dp[idx][prev_idx + 1] = max(
                pick,
                not_pick
            )

    return dp[0][0]


print(lis_tab(arr))

# =========================================================
# LONGEST INCREASING SUBSEQUENCE
# CLASSIC O(n²) DP
# =========================================================


def lis(arr):

    n = len(arr)

    # dp[i]
    # means:
    # length of LIS
    # ending at index i

    # every element alone
    # is an LIS of length 1
    dp = [1] * n

    # stores overall LIS length
    maxi = 1

    # build LIS
    for i in range(n):

        # check all previous indices
        for prev in range(i):

            # increasing condition
            if arr[prev] < arr[i]:

                # extend previous LIS
                dp[i] = max(
                    dp[i],
                    1 + dp[prev]
                )

        # update global maximum
        maxi = max(maxi, dp[i])

    return maxi


arr = [10, 9, 2, 5, 3, 7, 101, 18]

print(lis(arr))

# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def lis_space_optimized(arr):

    n = len(arr)

    next_row = [0] * (n + 1)

    # fill backwards
    for idx in range(n - 1, -1, -1):

        curr = [0] * (n + 1)

        for prev_idx in range(idx - 1, -2, -1):

            # not-pick
            not_pick = next_row[prev_idx + 1]

            # pick
            pick = 0

            if (
                prev_idx == -1
                or
                arr[idx] > arr[prev_idx]
            ):

                pick = 1 + next_row[idx + 1]

            curr[prev_idx + 1] = max(
                pick,
                not_pick
            )

        next_row = curr

    return next_row[0]


print(lis_space_optimized(arr))

