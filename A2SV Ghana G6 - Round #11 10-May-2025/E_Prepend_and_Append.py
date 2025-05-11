t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    left = 0
    right = n - 1

    while left < right:
        if (s[left] == '0' and s[right] == '1') or (s[left] == '1' and s[right] == '0'):
            n -= 2
            left += 1
            right -= 1
        
        else:
            break
    
    print(n)