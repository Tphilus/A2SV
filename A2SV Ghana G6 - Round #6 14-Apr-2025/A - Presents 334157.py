# Problem: A - Presents - https://codeforces.com/gym/601409/problem/A

n = int(input())
present_given = list(map(int, input().split()))

result_list = [0] * n

for i in range(n):
    receiver = present_given[i]
    result_list[receiver - 1] = i + 1

print(*result_list)
# ans = " ".join(map(str, result_list))
# print(ans)