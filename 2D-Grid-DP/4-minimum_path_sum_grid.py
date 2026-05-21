# RECURSION
def min_path(i, j, grid):

    # source reached
    if i == 0 and j == 0:
        return grid[0][0]

    # out of bounds
    if i < 0 or j < 0:
        return float('inf')

    up = grid[i][j] + min_path(i - 1, j, grid)

    left = grid[i][j] + min_path(i, j - 1, grid)

    return min(up, left)


grid = [
    [5, 9, 6],
    [11, 5, 2]
]

m = len(grid)
n = len(grid[0])

print(min_path(m - 1, n - 1, grid))


# MEMOIZATION
def min_path_memo(i, j, grid, dp):

    # source reached
    if i == 0 and j == 0:
        return grid[0][0]

    # out of bounds
    if i < 0 or j < 0:
        return float('inf')

    if dp[i][j] != -1:
        return dp[i][j]

    up = grid[i][j] + min_path_memo(i - 1, j, grid, dp)

    left = grid[i][j] + min_path_memo(i, j - 1, grid, dp)

    dp[i][j] = min(up, left)

    return dp[i][j]


dp = [[-1] * n for _ in range(m)]

print(min_path_memo(m - 1, n - 1, grid, dp))


# TABULATION
def min_path_tab(grid):

    m = len(grid)
    n = len(grid[0])

    dp = [[0] * n for _ in range(m)]

    for i in range(m):

        for j in range(n):

            # source
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
                continue

            up = float('inf')
            left = float('inf')

            if i > 0:
                up = grid[i][j] + dp[i - 1][j]

            if j > 0:
                left = grid[i][j] + dp[i][j - 1]

            dp[i][j] = min(up, left)

    return dp[m - 1][n - 1]


print(min_path_tab(grid))


# SPACE OPTIMIZATION
def min_path_space_optimized(grid):

    m = len(grid)
    n = len(grid[0])

    prev = [0] * n

    for i in range(m):

        curr = [0] * n

        for j in range(n):

            # source
            if i == 0 and j == 0:
                curr[j] = grid[i][j]

            else:

                up = float('inf')
                left = float('inf')

                if i > 0:
                    up = grid[i][j] + prev[j]

                if j > 0:
                    left = grid[i][j] + curr[j - 1]

                curr[j] = min(up, left)

        prev = curr

    return prev[n - 1]


print(min_path_space_optimized(grid))