def rob(nums):

    n = len(nums)

    # Edge case
    if n == 1:
        return nums[0]

    # Case 1: Exclude last
    case1 = rob_linear(nums[:-1])

    # Case 2: Exclude first
    case2 = rob_linear(nums[1:])

    return max(case1, case2)


def rob_linear(nums):

    prev = nums[0]
    prev2 = 0

    for i in range(1, len(nums)):

        pick = nums[i] + prev2

        not_pick = prev

        current = max(pick, not_pick)

        prev2 = prev
        prev = current

    return prev


nums = [2, 3, 2]

print(rob(nums))