# -----------------------------------
# TABULATION
# -----------------------------------

def longest_common_substring(s1, s2):

    n = len(s1)
    m = len(s2)

    # dp[i][j]
    # means:
    # length of longest common substring
    # ending at:
    # s1[i-1] and s2[j-1]

    # shifted indexing used
    # row 0 and column 0 represent empty string

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # stores overall maximum substring length
    maxi = 0

    # fill DP table
    for i in range(1, n + 1):

        for j in range(1, m + 1):

            # characters match
            if s1[i - 1] == s2[j - 1]:

                # extend previous substring
                dp[i][j] = 1 + dp[i - 1][j - 1]

                # update maximum answer
                maxi = max(maxi, dp[i][j])

            else:

                # substring continuity breaks
                dp[i][j] = 0

    return maxi


s1 = "abcdgh"
s2 = "acdghr"

print(longest_common_substring(s1, s2))

# -----------------------------------
# SPACE OPTIMIZATION
# -----------------------------------

def longest_common_substring_space_optimized(s1, s2):

    n = len(s1)
    m = len(s2)

    prev = [0] * (m + 1)

    maxi = 0

    for i in range(1, n + 1):

        curr = [0] * (m + 1)

        for j in range(1, m + 1):

            # characters match
            if s1[i - 1] == s2[j - 1]:

                curr[j] = 1 + prev[j - 1]

                maxi = max(maxi, curr[j])

            else:

                # substring breaks
                curr[j] = 0

        prev = curr

    return maxi


print(longest_common_substring_space_optimized(s1, s2))