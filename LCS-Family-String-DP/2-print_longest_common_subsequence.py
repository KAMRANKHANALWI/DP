def print_lcs(s1, s2):

    n = len(s1)
    m = len(s2)

    # dp[i][j]
    # means:
    # LCS length between:
    # first i chars of s1
    # first j chars of s2

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # fill DP table
    for i in range(1, n + 1):

        for j in range(1, m + 1):

            # characters match
            if s1[i - 1] == s2[j - 1]:

                # diagonal + 1
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                # take maximum from:
                # top or left
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # backtracking starts
    i = n
    j = m

    lcs = []

    # move until one string exhausted
    while i > 0 and j > 0:

        # characters match
        if s1[i - 1] == s2[j - 1]:

            # character part of LCS
            lcs.append(s1[i - 1])

            # move diagonally
            i -= 1
            j -= 1

        else:

            # move toward larger value

            # move upward
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1

            # move left
            else:
                j -= 1

    # reverse because built backwards
    lcs.reverse()

    return "".join(lcs)


s1 = "abcde"
s2 = "ace"

print("Longest Common Subsequence:", print_lcs(s1, s2))
