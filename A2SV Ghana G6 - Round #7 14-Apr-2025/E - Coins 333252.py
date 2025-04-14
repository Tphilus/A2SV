# Problem: E - Coins - https://codeforces.com/gym/602997/problem/E

for _ in range(int(input())):
    n, k = map(int, input().split())

    def c_coins(n, k):
        if n % 2 == 0 or (n - k) % 2 == 0 :
            return "YES"
        return "NO"
    print(c_coins(n,k))