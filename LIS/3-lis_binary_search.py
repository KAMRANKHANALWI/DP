# =========================================================
# LONGEST INCREASING SUBSEQUENCE
# BINARY SEARCH OPTIMIZATION
# O(n log n)
# =========================================================

from bisect import bisect_left


def lis_binary_search(arr):

    # temp
    # stores:
    # smallest possible tail
    # for increasing subsequences
    # of different lengths

    temp = []

    for num in arr:

        # if current number greater
        # than last element
        # extend LIS
        if (
            not temp
            or
            num > temp[-1]
        ):

            temp.append(num)

        else:

            # find first element
            # >= current number

            idx = bisect_left(temp, num)

            # replace element
            # to maintain smaller tail
            temp[idx] = num

    # length of temp
    # equals LIS length
    return len(temp)


arr = [10, 9, 2, 5, 3, 7, 101, 18]

print(lis_binary_search(arr))


# -----------------------------------
# LOWER BOUND
# first index with value >= target
# -----------------------------------

def lower_bound(arr, target):

    low = 0
    high = len(arr) - 1

    ans = len(arr)

    while low <= high:

        mid = (low + high) // 2

        # possible answer found
        if arr[mid] >= target:

            ans = mid

            # search smaller index
            high = mid - 1

        else:

            low = mid + 1

    return ans