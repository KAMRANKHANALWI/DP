# RECURSION
def triangle_path(i, j, triangle, n):

    # base case
    if i == n - 1:
        return triangle[i][j]

    down = triangle[i][j] + triangle_path(i + 1, j, triangle, n)

    diagonal = triangle[i][j] + triangle_path(i + 1, j + 1, triangle, n)

    return min(down, diagonal)

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
n = len(triangle)
print(triangle_path(0, 0, triangle, n))


# MEMOIZATION
def triangle_memo(i, j, triangle, n, dp):

    if i == n - 1:
        return triangle[i][j]

    if dp[i][j] != -1:
        return dp[i][j]

    down = triangle[i][j] + triangle_memo(i + 1, j, triangle, n, dp)

    diagonal = triangle[i][j] + triangle_memo(i + 1, j + 1, triangle, n, dp)

    dp[i][j] = min(down, diagonal)

    return dp[i][j]

# dp = [[-1] * n for _ in range(n)]
dp = [[-1] * len(row) for row in triangle]
print(triangle_memo(0,0,triangle, n, dp))


# TABULATION
def triangle_tab(triangle):

    n = len(triangle)

    dp = [[0] * n for _ in range(n)]

    # copy last row
    for j in range(n):
        dp[n - 1][j] = triangle[n - 1][j]

    # bottom to top
    for i in range(n - 2, -1, -1):

        for j in range(i + 1):

            down = dp[i + 1][j]

            diagonal = dp[i + 1][j + 1]

            dp[i][j] = triangle[i][j] + min(down, diagonal)

    return dp[0][0]

print(triangle_tab(triangle))


# SPACE OPTIMIZATION
def triangle_space(triangle):

    n = len(triangle)

    front = triangle[n - 1][:]

    for i in range(n - 2, -1, -1):

        curr = [0] * (i + 1)

        for j in range(i + 1):

            down = front[j]

            diagonal = front[j + 1]

            curr[j] = triangle[i][j] + min(down, diagonal)

        front = curr

    return front[0]

print(triangle_space(triangle))

