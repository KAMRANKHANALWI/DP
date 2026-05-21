def climb_stairs_memo(n, dp):
    if n <= 1:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = climb_stairs_memo(n - 1, dp) + climb_stairs_memo(n - 2, dp)

    return dp[n]


def climb_stairs_tabulation(n):
    if n <= 1:
        return 1

    dp = [-1] * (n + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_stairs_space_optimized(n):
    if n <= 1:
        return 1

    prev2 = 1
    prev = 1

    for i in range(2, n + 1):
        curi = prev + prev2

        prev2 = prev
        prev = curi

    return prev


n = int(input("Enter n: "))

# Memoization
dp = [-1] * (n + 1)
print("Memoization:", climb_stairs_memo(n, dp))

# Tabulation
print("Tabulation:", climb_stairs_tabulation(n))

# Space Optimized
print("Space Optimized:", climb_stairs_space_optimized(n))
