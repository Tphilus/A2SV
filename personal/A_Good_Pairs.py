# num of test cases
t = int(input())

for _ in range(t):
    # other input
    n = int(input())
    arr = list(map(int, input().split()))

    #[3,7,4,5,6] max - min = 4, 7-3
    # [0,0]

    smallest_idx = 0 
    largest_idx = 0

    for i in range(n):
        if arr[i] < arr[smallest_idx]:
            smallest_idx = i

        if arr[i] > arr[largest_idx]:
            largest_idx = i
        
    print(smallest_idx + 1, largest_idx + 1)