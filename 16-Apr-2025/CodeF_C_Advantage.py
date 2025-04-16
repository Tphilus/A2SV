t = int(input())
 
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
 
    sorted_s = sorted(s)
 
    result = []
 
    for i in range(n):
        if s[i] == sorted_s[-1]:
            result.append(s[i] - sorted_s[-2])
        else:
            result.append(s[i] - sorted_s[-1])
 
    print(*result)