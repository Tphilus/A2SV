def validMountainArray(arr):
    size = len(arr)
    # peak = 0

    # if n < 3:
    #     return False
    
    
    # for i in range(n-1):
    #     if arr[i] < arr[i + 1]:
    #         continue

    #     if arr[i] == arr[i + 1]:
    #         return False
        
    #     if arr[i] > arr[i + 1]:
    #         peak = i
    #         break


    # # after finding the peak n -1

    # for j in range(peak, n -1):
    #     if arr[i] < arr[i + 1]:
    #         continue

    #     if arr[i] == arr[i + 1]:
    #         return False
        
    # return True

    """
    left stritly acending
    right stritly decending
    peak in the middle 
    """

    # look for the peak
    # check left side
    # check right side
    # Return True 

    # decending = False
    # acending = False

    # i = 0

    # while (i + 1) < size and arr[i] < arr[i + 1]:
    #     acending = True
    #     i += 1

    # while (i + 1) < size and arr[i] > arr[i + 1]:
    #     decending = True
    #     i += 1

    # return acending and decending and i == size - 1  

    if size < 3:
        return False
    
    left_idx, right_idx = 0, size - 1

    while left_idx + 1 < size - 1 and arr[left_idx] < arr[left_idx + 1]:
        left_idx += 1
    
    while right_idx - 1 > 0 and arr[right_idx] < arr[right_idx - 1]:
        right_idx -= 1
    return left_idx == right_idx

# print(validMountainArray([3,5,5])) # False
print(validMountainArray([0,3,2,1]))