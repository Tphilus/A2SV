
def countingSort(nums):
    max_num = max(nums)

    count = [0] * (max_num + 1)

    for num in nums:
        count[num] += 1


    target = 0

    for idx, value in enumerate(count):
        for i in range(value):
            nums[target] = idx
            target += 1

    return nums

nums = [-2, -3, -3, -5, 5,3,3,2,3,4,2,5,1]
print(countingSort(nums))