nums = [3,1,2,2,2,1,3]
k = 2

result = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j] and i * j % k == 0:
            result += 1

print(result)
