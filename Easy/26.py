def removeDuplicates(nums):
    if not nums:
        return 0

    unique = []
    k = 0

    for num in nums:
        if num not in unique:
            unique.append(num)
            k += 1

    return unique


list = [1,2,9,49,5,3,1,1,1,5,9,4,5]
print(removeDuplicates(list))