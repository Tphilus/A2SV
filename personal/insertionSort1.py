def insertionSort1(n, arr):
    # Write your code here
    key = arr[n - 1]
    i = n - 2
    
    # Shift elements of arr[0..i] that are greater than key to one position ahead
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        print(*arr) # Print the array after each shift
        i -= 1
    
    # Insert the key at the correct position
    arr[i + 1] = key
    print(*arr) 