def countingSort(arr):
    # Write your code here
    frequency = [0] * 100
    
    for num in arr:
        frequency[num] += 1
    
    return frequency