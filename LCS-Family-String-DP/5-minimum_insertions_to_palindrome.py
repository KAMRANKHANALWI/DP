# -----------------------------------
# TABULATION
# -----------------------------------

def minimum_insertions_to_palindrome(s):

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

    # longest palindromic subsequence length
    lps = dp[n][n]

    # minimum insertions needed
    return n - lps


s = "abcaa"

print(minimum_insertions_to_palindrome(s))

# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def minimum_insertions_to_palindrome_space_optimized(s):

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

    # LPS length
    lps = prev[n]

    # minimum insertions
    return n - lps


print(minimum_insertions_to_palindrome_space_optimized(s))