n = int(input())
lst = list(map(int, input().split()))
print("input: ",n)
print("list: ",lst)

for i in range(len(lst)):
    if n < lst[i]:
        print("YES")
        n += 1
    else:
        print("NO")