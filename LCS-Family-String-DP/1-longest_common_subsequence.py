# -----------------------------------
# RECURSION
# -----------------------------------

def lcs(i, j, s1, s2):

    # one string exhausted
    # no common subsequence possible
    if i < 0 or j < 0:
        return 0

    # characters match
    if s1[i] == s2[j]:

        # include current character
        # move diagonally
        return 1 + lcs(
            i - 1,
            j - 1,
            s1,
            s2
        )

    # characters do not match

    # skip current character from s1
    left = lcs(
        i - 1,
        j,
        s1,
        s2
    )

    # skip current character from s2
    right = lcs(
        i,
        j - 1,
        s1,
        s2
    )

    # take maximum LCS length
    return max(left, right)


s1 = "abcde"
s2 = "ace"

n = len(s1)
m = len(s2)

print(lcs(n - 1, m - 1, s1, s2))


# -----------------------------------
# MEMOIZATION
# -----------------------------------

def lcs_memo(i, j, s1, s2, dp):

    # one string exhausted
    if i < 0 or j < 0:
        return 0

    # dp[i][j]
    # means:
    # LCS length between:
    # s1[0...i] and s2[0...j]

    # already solved
    if dp[i][j] != -1:
        return dp[i][j]

    # characters match
    if s1[i] == s2[j]:

        dp[i][j] = 1 + lcs_memo(
            i - 1,
            j - 1,
            s1,
            s2,
            dp
        )

        return dp[i][j]

    # characters do not match

    # skip character from s1
    left = lcs_memo(
        i - 1,
        j,
        s1,
        s2,
        dp
    )

    # skip character from s2
    right = lcs_memo(
        i,
        j - 1,
        s1,
        s2,
        dp
    )

    # store maximum answer
    dp[i][j] = max(left, right)

    return dp[i][j]


dp = [[-1] * m for _ in range(n)]

print(lcs_memo(n - 1, m - 1, s1, s2, dp))


# -----------------------------------
# TABULATION
# -----------------------------------

def lcs_tab(s1, s2):

    n = len(s1)
    m = len(s2)

    # dp[i][j]
    # means:
    # LCS length between:
    # first i characters of s1
    # first j characters of s2

    # shifted indexing used
    # row 0 and column 0 represent empty string

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # first row and first column already 0
    # because LCS with empty string = 0

    # fill remaining table
    for i in range(1, n + 1):

        for j in range(1, m + 1):

            # characters match
            if s1[i - 1] == s2[j - 1]:

                # take diagonal + 1
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                # skip from s1
                left = dp[i - 1][j]

                # skip from s2
                right = dp[i][j - 1]

                # take maximum
                dp[i][j] = max(left, right)

    return dp[n][m]


print(lcs_tab(s1, s2))


# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def lcs_space_optimized(s1, s2):

    n = len(s1)
    m = len(s2)

    # prev[j]
    # means:
    # previous row LCS values

    prev = [0] * (m + 1)

    for i in range(1, n + 1):

        curr = [0] * (m + 1)

        for j in range(1, m + 1):

            # characters match
            if s1[i - 1] == s2[j - 1]:

                # diagonal + 1
                curr[j] = 1 + prev[j - 1]

            else:

                # top cell
                left = prev[j]

                # left cell
                right = curr[j - 1]

                # take maximum
                curr[j] = max(left, right)

        prev = curr

    return prev[m]


print(lcs_space_optimized(s1, s2))