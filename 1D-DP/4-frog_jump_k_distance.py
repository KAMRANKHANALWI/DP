def frog_jump_k(i, heights, k):
    if i == 0:
        return 0

    min_energy = float("inf")

    for j in range(1, k + 1):

        if i - j >= 0:

            jump_cost = frog_jump_k(i - j, heights, k) + abs(
                heights[i] - heights[i - j]
            )

            min_energy = min(min_energy, jump_cost)

    return min_energy


def frog_jump_k_memo(i, heights, k, dp):
    if i == 0:
        return 0

    if dp[i] != -1:
        return dp[i]

    min_energy = float("inf")

    for j in range(1, k + 1):

        if i - j >= 0:

            jump_cost = frog_jump_k_memo(i - j, heights, k, dp) + abs(
                heights[i] - heights[i - j]
            )

            min_energy = min(min_energy, jump_cost)

    dp[i] = min_energy

    return dp[i]


def frog_jump_k_tabulation(heights, k):
    n = len(heights)

    dp = [0] * n

    for i in range(1, n):

        min_energy = float("inf")

        for j in range(1, k + 1):

            if i - j >= 0:

                jump_cost = dp[i - j] + abs(heights[i] - heights[i - j])

                min_energy = min(min_energy, jump_cost)

        dp[i] = min_energy

    return dp[n - 1]


heights = [10, 30, 40, 50, 20]
k = 3

n = len(heights)

# Recursive
print("Recursive:", frog_jump_k(n - 1, heights, k))

# Memoization
dp = [-1] * n
print("Memoization:", frog_jump_k_memo(n - 1, heights, k, dp))

# Tabulation
print("Tabulation:", frog_jump_k_tabulation(heights, k))
