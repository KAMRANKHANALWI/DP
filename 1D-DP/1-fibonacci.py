def fib_memo(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = fib_memo(n - 1, dp) + fib_memo(n - 2, dp)
    return dp[n]


def fib_tabulation(n):
    if n <= 1:
        return n

    dp = [-1] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fib_space_optimized(n):
    if n <= 1:
        return n

    prev2 = 0
    prev = 1

    for i in range(2, n + 1):
        curi = prev + prev2
        prev2 = prev
        prev = curi

    return prev


n = int(input("Enter a number: "))

# Memoization
dp = [-1] * (n + 1)
print("Memoization:", fib_memo(n, dp))

# Tabulation
print("Tabulation:", fib_tabulation(n))

# Space Optimized
print("Space Optimized:", fib_space_optimized(n))
