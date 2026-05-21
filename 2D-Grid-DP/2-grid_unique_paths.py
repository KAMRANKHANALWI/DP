def path(i, j):
    if i == 0 and j == 0:
        return 1

    if i < 0 or j < 0:
        return 0

    up = path(i - 1, j)
    left = path(i, j - 1)
    return up + left


m = 3
n = 2
print(path(m - 1, n - 1))


def path_memo(i, j, dp):
    if i == 0 and j == 0:
        return 1

    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    up = path_memo(i - 1, j, dp)
    left = path_memo(i, j - 1, dp)
    dp[i][j] = up + left
    return dp[i][j]


dp = [[-1] * n for _ in range(m)]
m = 3
n = 2
print(path_memo(m - 1, n - 1, dp))


def path_tab(m, n):
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = 1

    for i in range(m):
        for j in range(n):

            if i == 0 and j == 0:
                continue

            up = 0
            left = 0

            if i > 0:
                up = dp[i - 1][j]

            if j > 0:
                left = dp[i][j - 1]

            dp[i][j] = up + left

    return dp[m - 1][n - 1]


m = 3
n = 2
print(path_tab(m, n))


def unique_paths_space_optimized(m, n):
    prev = [0] * n

    for i in range(m):
        curr = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                curr[j] = 1
            else:
                up = 0
                left = 0

                if i > 0:
                    up = prev[j]

                if j > 0:
                    left = curr[j - 1]

                curr[j] = up + left

        prev = curr
    return prev[n - 1]


m = 3
n = 2
print(unique_paths_space_optimized(m, n))
