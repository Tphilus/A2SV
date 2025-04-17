# Problem: Wrong Subtraction - https://codeforces.com/problemset/problem/977/A?mobile=false

def wrong_subtraction(n, k):
    for _ in range(k):
        if n % 10 == 0:
            n //= 10  # Remove the last digit
        else:
            n -= 1  # Subtract 1 from the number
    return n


n, k = map(int, input().split())
result = wrong_subtraction(n, k)
print(result)
