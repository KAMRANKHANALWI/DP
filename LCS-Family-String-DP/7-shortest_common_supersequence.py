# -----------------------------------
# TABULATION + BACKTRACKING
# -----------------------------------

def shortest_common_supersequence(s1, s2):

    n = len(s1)
    m = len(s2)

    # dp[i][j]
    # means:
    # LCS length between:
    # first i chars of s1
    # first j chars of s2

    # shifted indexing used
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # build LCS table
    for i in range(1, n + 1):

        for j in range(1, m + 1):

            # characters match
            if s1[i - 1] == s2[j - 1]:

                # diagonal + 1
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                # take maximum
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    # backtracking starts
    i = n
    j = m

    scs = []

    while i > 0 and j > 0:

        # characters match
        if s1[i - 1] == s2[j - 1]:

            # add only once
            scs.append(s1[i - 1])

            # move diagonally
            i -= 1
            j -= 1

        else:

            # move toward larger LCS value

            # move upward
            if dp[i - 1][j] > dp[i][j - 1]:

                # add character from s1
                scs.append(s1[i - 1])

                i -= 1

            else:

                # add character from s2
                scs.append(s2[j - 1])

                j -= 1

    # remaining characters from s1
    while i > 0:

        scs.append(s1[i - 1])
        i -= 1

    # remaining characters from s2
    while j > 0:

        scs.append(s2[j - 1])
        j -= 1

    # built backwards
    scs.reverse()

    return "".join(scs)


s1 = "brute"
s2 = "groot"

print(shortest_common_supersequence(s1, s2))

