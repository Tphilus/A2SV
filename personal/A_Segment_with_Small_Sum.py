n,s = map(int, input().split())
arr_a = list(map(int, input().split()))

def Segment_with_Small_Sum(arr_a):

    left = 0
    result = 0
    max_len = 0

    for right in range(n):
        result += arr_a[right]

        while result > s:
            result -= arr_a[left]
            left += 1
        
        max_len = max(right - left + 1 , max_len)
    
    return max_len

print(Segment_with_Small_Sum(arr_a))
