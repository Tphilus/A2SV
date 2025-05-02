t = int(input())
for _ in range(t):
    n = int(input())
    arr_a = list(map(int, input().split()))

    res = []
    start = 0
    end = len(arr_a) - 1

    for i in range(n):
        if i % 2 == 0:
            res.append(arr_a[start])
            start += 1
        else:
            res.append(arr_a[end])
            end -= 1
    
    print(*res)