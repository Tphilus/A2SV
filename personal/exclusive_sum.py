def exclusive_sum(arr):
    prefix = []
    cur_num  = 0

    for i in range(len(arr)):
        prefix.append(cur_num)
        cur_num += arr[i]
    return prefix
    
arr = [2, 3, 4, 3, 2, 1]
print(exclusive_sum(arr))