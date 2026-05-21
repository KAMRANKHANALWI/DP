def rob(i, nums):

    # Base case
    if i == 0:
        return nums[0]

    # Out of bounds
    if i < 0:
        return 0

    # Rob current house
    pick = nums[i] + rob(i - 2, nums)

    # Skip current house
    not_pick = rob(i - 1, nums)

    return max(pick, not_pick)


nums = [2, 7, 9, 3, 1]

n = len(nums)

print(rob(n - 1, nums))

def rob_memo(i, nums, dp):

    if i == 0:
        return nums[0]

    if i < 0:
        return 0

    # Already solved
    if dp[i] != -1:
        return dp[i]

    pick = nums[i] + rob_memo(i - 2, nums, dp)

    not_pick = rob_memo(i - 1, nums, dp)

    dp[i] = max(pick, not_pick)

    return dp[i]


nums = [2, 7, 9, 3, 1]

n = len(nums)

dp = [-1] * n

print(rob_memo(n - 1, nums, dp))

def rob_tab(nums):

    n = len(nums)

    dp = [0] * n

    dp[0] = nums[0]

    for i in range(1, n):

        # Rob current house
        pick = nums[i]

        if i > 1:
            pick += dp[i - 2]

        # Skip current house
        not_pick = dp[i - 1]

        dp[i] = max(pick, not_pick)

    return dp[n - 1]


nums = [2, 7, 9, 3, 1]

print(rob_tab(nums))

def rob_optimized(nums):

    n = len(nums)

    prev = nums[0]
    prev2 = 0

    for i in range(1, n):

        pick = nums[i] + prev2

        not_pick = prev

        current = max(pick, not_pick)

        prev2 = prev
        prev = current

    return prev


nums = [2, 7, 9, 3, 1]

print(rob_optimized(nums))