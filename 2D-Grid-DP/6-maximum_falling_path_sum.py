# -----------------------------------
# RECURSION
# -----------------------------------

def falling_path(i, j, matrix, m):

    # out of bounds
    if j < 0 or j >= m:
        return float('-inf')

    # reached first row
    if i == 0:
        return matrix[0][j]

    up = matrix[i][j] + falling_path(i - 1, j, matrix, m)

    left_diagonal = matrix[i][j] + falling_path(i - 1, j - 1, matrix, m)

    right_diagonal = matrix[i][j] + falling_path(i - 1, j + 1, matrix, m)

    return max(up, left_diagonal, right_diagonal)


matrix = [
    [1, 2, 10, 4],
    [100, 3, 2, 1],
    [1, 1, 20, 2],
    [1, 2, 2, 1]
]

n = len(matrix)
m = len(matrix[0])

maxi = float('-inf')

# variable ending point
for j in range(m):
    maxi = max(maxi, falling_path(n - 1, j, matrix, m))

print(maxi)


# -----------------------------------
# MEMOIZATION
# -----------------------------------

def falling_path_memo(i, j, matrix, m, dp):

    # out of bounds
    if j < 0 or j >= m:
        return float('-inf')

    # reached first row
    if i == 0:
        return matrix[0][j]

    if dp[i][j] != -1:
        return dp[i][j]

    up = matrix[i][j] + falling_path_memo(i - 1, j, matrix, m, dp)

    left_diagonal = matrix[i][j] + falling_path_memo(i - 1, j - 1, matrix, m, dp)

    right_diagonal = matrix[i][j] + falling_path_memo(i - 1, j + 1, matrix, m, dp)

    dp[i][j] = max(up, left_diagonal, right_diagonal)

    return dp[i][j]


dp = [[-1] * m for _ in range(n)]

maxi = float('-inf')

for j in range(m):
    maxi = max(maxi, falling_path_memo(n - 1, j, matrix, m, dp))

print(maxi)


# -----------------------------------
# TABULATION
# -----------------------------------

def falling_path_tab(matrix):

    n = len(matrix)
    m = len(matrix[0])

    dp = [[0] * m for _ in range(n)]

    # base case -> first row
    for j in range(m):
        dp[0][j] = matrix[0][j]

    # top to bottom
    for i in range(1, n):

        for j in range(m):

            up = matrix[i][j] + dp[i - 1][j]

            left_diagonal = matrix[i][j]
            if j > 0:
                left_diagonal += dp[i - 1][j - 1]
            else:
                left_diagonal += float('-inf')

            right_diagonal = matrix[i][j]
            if j < m - 1:
                right_diagonal += dp[i - 1][j + 1]
            else:
                right_diagonal += float('-inf')

            dp[i][j] = max(up, left_diagonal, right_diagonal)

    # variable ending point
    return max(dp[n - 1])


print(falling_path_tab(matrix))


# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def falling_path_space_optimized(matrix):

    n = len(matrix)
    m = len(matrix[0])

    prev = matrix[0][:]

    for i in range(1, n):

        curr = [0] * m

        for j in range(m):

            up = matrix[i][j] + prev[j]

            left_diagonal = matrix[i][j]

            if j > 0:
                left_diagonal += prev[j - 1]
            else:
                left_diagonal += float('-inf')

            right_diagonal = matrix[i][j]

            if j < m - 1:
                right_diagonal += prev[j + 1]
            else:
                right_diagonal += float('-inf')

            curr[j] = max(up, left_diagonal, right_diagonal)

        prev = curr

    return max(prev)


print(falling_path_space_optimized(matrix))