def ninja(day, last, points):
    if day == 0:
        maxi = 0

        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])

        return maxi

    maxi = 0
    for task in range(3):
        if task != last:
            activity = points[day][task] + ninja(day - 1, task, points)
            maxi = max(maxi, activity)

    return maxi


points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]

n = len(points)

print(ninja(n - 1, 3, points))  # 3 = no previous activity: used initially


def ninja_memo(day, last, points, dp):
    if day == 0:
        maxi = 0
        for task in range(3):
            if task != last:
                maxi = max(maxi, points[0][task])
        return maxi

    if dp[day][last] != -1:
        return dp[day][last]

    maxi = 0
    for task in range(3):
        if task != last:
            activity = points[day][task] + ninja_memo(day - 1, task, points, dp)
            maxi = max(maxi, activity)
    dp[day][last] = maxi
    return maxi


points = [[10, 40, 70], [20, 50, 80], [30, 60, 90]]

n = len(points)

dp = [[-1] * 4 for _ in range(n)]

print(ninja_memo(n - 1, 3, points, dp))


def ninja_tab(points):

    n = len(points)

    dp = [[0] * 4 for _ in range(n)]

    # Base case for day 0
    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0])

    for day in range(1, n):

        for last in range(4):

            dp[day][last] = 0

            for task in range(3):

                if task != last:

                    activity = (
                        points[day][task]
                        + dp[day - 1][task]
                    )

                    dp[day][last] = max(
                        dp[day][last],
                        activity
                    )

    return dp[n - 1][3]


points = [
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
]

print(ninja_tab(points))

def ninja_space(points):

    n = len(points)

    prev = [0] * 4

    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0])

    for day in range(1, n):

        temp = [0] * 4

        for last in range(4):

            for task in range(3):

                if task != last:

                    activity = (
                        points[day][task]
                        + prev[task]
                    )

                    temp[last] = max(
                        temp[last],
                        activity
                    )

        prev = temp

    return prev[3]


points = [
    [10, 40, 70],
    [20, 50, 80],
    [30, 60, 90]
]

print(ninja_space(points))