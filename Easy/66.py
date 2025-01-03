def plusOne(digits):
    if not digits:
        return 0

    n = -1
    is_running = True
    plus_one = False


    if digits[n] == 9:
        nums = digits[-1] + 1
        for i in range(len(digits) - 1):
            n -= 1
            if digits[n] == 9:
                nums *= (digits[n] + 1)
            else:
                plus_one = digits[n] + 1
                break

        digits = digits[:n] + [int(i) for i in str(nums)]

        if plus_one:
            digits[n] = plus_one

    else:
        digits[-1] = digits[-1] + 1

    return digits

num = [9,8,9]
print(plusOne(num))