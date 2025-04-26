def max_alternating_sum(arr):
    n = len(arr)
    res = 0
    idx = 0
    while idx < n:
        current = arr[idx]
        j = idx
        while j < n and (arr[j] > 0) == (current > 0):
            current = max(current, arr[j])
            j += 1
        res += current
        idx = j
    return res

# Reading input
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(max_alternating_sum(a))