def climbStairs(n):
    if n == 0:
        return 0

    one, two = 1, 1

    for i in range(n - 1):
        temp = one
        one += two
        two = temp

    return one