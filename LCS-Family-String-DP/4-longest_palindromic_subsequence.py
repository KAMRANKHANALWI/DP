# -----------------------------------
# TABULATION
# -----------------------------------

def longest_palindromic_subsequence(s):

    # reverse string
    rev = s[::-1]

    n = len(s)

    # dp[i][j]
    # means:
    # LCS length between:
    # first i chars of s
    # first j chars of reversed string

    # shifted indexing used
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # first row and first column already 0
    # because empty string LCS = 0

    # fill DP table
    for i in range(1, n + 1):

        for j in range(1, n + 1):

            # characters match
            if s[i - 1] == rev[j - 1]:

                # include character
                # move diagonally
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                # skip from original string
                left = dp[i - 1][j]

                # skip from reversed string
                right = dp[i][j - 1]

                # take maximum
                dp[i][j] = max(left, right)

    return dp[n][n]


s = "bbabcbcab"

print(longest_palindromic_subsequence(s))

# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def longest_palindromic_subsequence_space_optimized(s):

    rev = s[::-1]

    n = len(s)

    # prev[j]
    # means:
    # previous row LCS values

    prev = [0] * (n + 1)

    for i in range(1, n + 1):

        curr = [0] * (n + 1)

        for j in range(1, n + 1):

            # characters match
            if s[i - 1] == rev[j - 1]:

                curr[j] = 1 + prev[j - 1]

            else:

                curr[j] = max(
                    prev[j],
                    curr[j - 1]
                )

        prev = curr

    return prev[n]


print(longest_palindromic_subsequence_space_optimized(s))