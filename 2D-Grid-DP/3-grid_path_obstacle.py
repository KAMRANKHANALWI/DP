# RECURSION
def maze(i, j, grid):

    # obstacle
    if i >= 0 and j >= 0 and grid[i][j] == -1:
        return 0

    # source reached
    if i == 0 and j == 0:
        return 1

    # out of bounds
    if i < 0 or j < 0:
        return 0

    up = maze(i - 1, j, grid)
    left = maze(i, j - 1, grid)

    return up + left


grid = [[0, 0, 0], [0, -1, 0], [0, 0, 0]]

m = len(grid)
n = len(grid[0])

print(maze(m - 1, n - 1, grid))


# MEMOIZATION
def maze_memo(i, j, grid, dp):

    # obstacle
    if i >= 0 and j >= 0 and grid[i][j] == -1:
        return 0

    # source reached
    if i == 0 and j == 0:
        return 1

    # out of bounds
    if i < 0 or j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    up = maze_memo(i - 1, j, grid, dp)
    left = maze_memo(i, j - 1, grid, dp)

    dp[i][j] = up + left

    return dp[i][j]


dp = [[-1] * n for _ in range(m)]

print(maze_memo(m - 1, n - 1, grid, dp))



# TABULATION
def maze_tab(grid):

    m = len(grid)
    n = len(grid[0])

    dp = [[0] * n for _ in range(m)]

    for i in range(m):

        for j in range(n):

            # obstacle
            if grid[i][j] == -1:
                dp[i][j] = 0
                continue

            # source
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue

            up = 0
            left = 0

            if i > 0:
                up = dp[i - 1][j]

            if j > 0:
                left = dp[i][j - 1]

            dp[i][j] = up + left

    return dp[m - 1][n - 1]


print(maze_tab(grid))



# SPACE OPTIMIZATION
def maze_space_optimized(grid):

    m = len(grid)
    n = len(grid[0])

    prev = [0] * n

    for i in range(m):

        curr = [0] * n

        for j in range(n):

            # obstacle
            if grid[i][j] == -1:
                curr[j] = 0

            # source
            elif i == 0 and j == 0:
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


print(maze_space_optimized(grid))
