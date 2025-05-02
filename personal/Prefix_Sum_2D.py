def prefix_sum_2D(matrix):
    prefix_sum = [[0 for _ in range(len(matrix[0])+1)] for _ in range(len(matrix)+1)]

    for rows in range(len(matrix)):
        for cols in range(len(matrix[0])):
            prefix_sum[rows+1][cols+1] = matrix[rows][cols] + prefix_sum[rows][cols+1] + prefix_sum[rows+1][cols] - prefix_sum[rows][cols]
    return prefix_sum


matrix = [
    [3, 5, 6, 10],
    [9, 18, 30, 43],
    [9, 30, 50, 78],
    [12, 32, 72, 98]
]

matrix_two = [
    [3, 2, 1, 4],
    [6, 7, 11, 9],
    [0, 12, 8, 15],
    [3, -1, 20, -2]
]
print(prefix_sum_2D(matrix_two))