# Recursive
def max_sum(i, arr):

    if i == 0:
        return arr[0]

    if i < 0:
        return 0

    # Pick current element
    pick = arr[i] + max_sum(i - 2, arr)

    # Do not pick current element
    not_pick = max_sum(i - 1, arr)

    return max(pick, not_pick)


# Memoization
def max_sum_memo(i, arr, dp):

    if i == 0:
        return arr[0]

    if i < 0:
        return 0

    if dp[i] != -1:
        return dp[i]

    # Pick current element
    pick = arr[i] + max_sum_memo(i - 2, arr, dp)

    # Do not pick current element
    not_pick = max_sum_memo(i - 1, arr, dp)

    dp[i] = max(pick, not_pick)

    return dp[i]


# Tabulation
def max_sum_tab(arr):

    n = len(arr)

    dp = [0] * n

    dp[0] = arr[0]

    for i in range(1, n):

        pick = arr[i]

        if i > 1:
            pick += dp[i - 2]

        not_pick = dp[i - 1]

        dp[i] = max(pick, not_pick)

    return dp[n - 1]


# Space Optimized
def max_sum_optimized(arr):

    n = len(arr)

    prev2 = 0
    prev = arr[0]

    for i in range(1, n):

        pick = arr[i] + prev2

        not_pick = prev

        curi = max(pick, not_pick)

        prev2 = prev
        prev = curi

    return prev


arr = [2, 1, 4, 9]

n = len(arr)

# Recursive
print("Recursive:", max_sum(n - 1, arr))

# Memoization
dp = [-1] * n
print("Memoization:", max_sum_memo(n - 1, arr, dp))

# Tabulation
print("Tabulation:", max_sum_tab(arr))

# Space Optimized
print("Space Optimized:", max_sum_optimized(arr))