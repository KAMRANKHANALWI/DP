# -----------------------------------
# TABULATION
# -----------------------------------

def min_insert_delete(s1, s2):

    n = len(s1)
    m = len(s2)

    # dp[i][j]
    # means:
    # LCS length between:
    # first i chars of s1
    # first j chars of s2

    # shifted indexing used
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # fill DP table
    for i in range(1, n + 1):

        for j in range(1, m + 1):

            # characters match
            if s1[i - 1] == s2[j - 1]:

                # include character
                # move diagonally
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                # skip from s1
                left = dp[i - 1][j]

                # skip from s2
                right = dp[i][j - 1]

                # take maximum
                dp[i][j] = max(left, right)

    # longest common subsequence length
    lcs = dp[n][m]

    # deletions needed from s1
    deletions = n - lcs

    # insertions needed into s1
    insertions = m - lcs

    return insertions + deletions


s1 = "heap"
s2 = "pea"

print(min_insert_delete(s1, s2))