# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
arr_one = list(map(int, input().split()))
arr_two = list(map(int, input().split()))

def merging_arrays(arr_one, arr_two):

    first = 0
    second = 0
    merge_arr = []

    while first < len(arr_one) and second < len(arr_two):
        if arr_one[first] < arr_two[second]:
            merge_arr.append(arr_one[first])
            first += 1
        else:
            merge_arr.append(arr_two[second])
            second += 1

    merge_arr.extend(arr_one[first:])
    merge_arr.extend(arr_two[second:])

    return merge_arr   

print(*merging_arrays(arr_one, arr_two)) 