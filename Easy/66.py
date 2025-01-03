def plusOne(digits):
    if not digits:
        return 0

    n = -1
    is_running = True
    plus_one = False

    #checks to see if the last element in the list is 9
    if digits[n] == 9:
        nums = digits[-1] + 1
        for i in range(len(digits) - 1): #itterate through the list incase there are other 9s in the list
            n -= 1
            if digits[n] == 9:              #if there is another 9 adds a 0 to the total
                nums *= (digits[n] + 1)
            else:                           #if there is a number other that a 9 plus_one is updated and adds one to the number
                plus_one = digits[n] + 1
                break

        digits = digits[:n] + [int(i) for i in str(nums)]  #adds the original list with the new one using slicing incase there are other numbers that wasnt touched

        if plus_one:                #if plus_one has a value it replaces the number that holds the index of the variable "n"
            digits[n] = plus_one

    else:
        digits[-1] = digits[-1] + 1  #if the number is not 9 it gets 1 adds to it

    return digits               # returns the list

num = [9,8,9]
print(plusOne(num))