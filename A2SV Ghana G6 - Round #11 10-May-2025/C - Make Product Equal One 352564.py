# Problem: C - Make Product Equal One - https://codeforces.com/gym/609159/problem/C

def min_count_to_make_product_one(n, arr):
    count = 0
    negative_count = 0
    zero_count = 0

    for num in arr:
        if num > 1:
            count += num - 1
        elif num < -1:
            count += abs(num + 1)
            negative_count += 1
        elif num == 0:
            zero_count += 1
            count += 1
        elif num == -1:
            negative_count += 1
        else:  # num == 1, no count
            continue

    if negative_count % 2 == 1:
        if zero_count == 0:
            count += 2

    return count

n = int(input())
arr = list(map(int, input().split()))
print(min_count_to_make_product_one(n, arr))
