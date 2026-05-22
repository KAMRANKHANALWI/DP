def print_lis(arr):

    n = len(arr)

    # dp[i]
    # means:
    # length of LIS
    # ending at index i

    # initially every element alone
    # is an LIS of length 1
    dp = [1] * n

    # hash_arr[i]
    # means:
    # previous index used
    # to build LIS ending at i

    # used later for reconstruction
    hash_arr = [0] * n

    # initially every element
    # points to itself
    for i in range(n):
        hash_arr[i] = i

    # stores overall LIS length
    maxi = 1

    # stores ending index of LIS
    last_index = 0

    # build dp array
    for i in range(n):

        # check all previous indices
        for prev in range(i):

            # increasing condition
            if arr[prev] < arr[i] and 1 + dp[prev] > dp[i]:

                # extend LIS
                dp[i] = 1 + dp[prev]

                # store previous index
                # from where LIS came
                hash_arr[i] = prev

        # update overall maximum LIS
        if dp[i] > maxi:

            maxi = dp[i]

            # store ending index
            last_index = i

    # -----------------------------------
    # RECONSTRUCTION
    # -----------------------------------

    lis = []

    # first add last element
    lis.append(arr[last_index])

    # move backwards
    # using hash array
    while hash_arr[last_index] != last_index:

        # jump to previous index
        last_index = hash_arr[last_index]

        # add element
        lis.append(arr[last_index])

    # currently built backwards
    lis.reverse()

    return lis


arr = [5, 4, 11, 1, 16, 8]

print(print_lis(arr))
