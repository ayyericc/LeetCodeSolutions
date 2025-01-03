def searchInsert(nums, target):
    low, high = 0, len(nums)

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid

    return low

nums = [1,3]
target = 3
print(searchInsert(nums,target))