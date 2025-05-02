t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    def c_coins(n, k):
        if n % 2 == 0 or (n - k) % 2 == 0 :
            return "YES"
        return "NO"
    print(c_coins(n,k))


# n = int(input())
# lst = list(map(int, input().split()))

# for i in range(len(lst) + 2):
#     if i + 1 == n or i != 2:
#     # if i + 1 == n and i == 3 or i != 2:
#         print("YES")
#     else:
#         print("NO")

