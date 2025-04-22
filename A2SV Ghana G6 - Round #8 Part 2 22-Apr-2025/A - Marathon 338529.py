# Problem: A - Marathon - https://codeforces.com/gym/604840/problem/A

t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))

    def marathon(arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] > arr[0]:
                count += 1
        return count   

    print(marathon(arr))