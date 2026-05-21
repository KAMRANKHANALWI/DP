def frog_jump_memo(i, heights, dp):
    if i == 0:
        return 0

    if dp[i] != -1:
        return dp[i]

    left = frog_jump_memo(i - 1, heights, dp) + abs(heights[i] - heights[i - 1])

    right = float("inf")

    if i > 1:
        right = frog_jump_memo(i - 2, heights, dp) + abs(heights[i] - heights[i - 2])

    dp[i] = min(left, right)

    return dp[i]


def frog_jump_tabulation(heights):
    n = len(heights)

    dp = [-1] * n
    dp[0] = 0

    for i in range(1, n):

        left = dp[i - 1] + abs(heights[i] - heights[i - 1])

        right = float("inf")

        if i > 1:
            right = dp[i - 2] + abs(heights[i] - heights[i - 2])

        dp[i] = min(left, right)

    return dp[n - 1]


def frog_jump_space_optimized(heights):
    n = len(heights)

    prev2 = 0
    prev = 0

    for i in range(1, n):

        left = prev + abs(heights[i] - heights[i - 1])

        right = float("inf")

        if i > 1:
            right = prev2 + abs(heights[i] - heights[i - 2])

        curi = min(left, right)

        prev2 = prev
        prev = curi

    return prev


heights = [0, 1, 3, 5, 6, 8, 12, 17]

n = len(heights)

# Memoization
dp = [-1] * n
print("Memoization:", frog_jump_memo(n - 1, heights, dp))

# Tabulation
print("Tabulation:", frog_jump_tabulation(heights))

# Space Optimized
print("Space Optimized:", frog_jump_space_optimized(heights))
