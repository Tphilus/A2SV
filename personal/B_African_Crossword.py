n,m = map(int, input().split())
# print(m)
# print(n)

matrix = [input() for _ in range(n)]
# print(matrix)
result = []

for i in range(n):
    for j in range(m):
        ch = matrix[i][j]
        row_count = 0
        col_count = 0

        for r in range(n):
            if matrix[r][j] == ch:
                col_count += 1

        for c in range(m):
            if matrix[i][c] == ch:
                row_count += 1

        if row_count == 1 and col_count == 1:
            result.append(ch)

print(*result,sep="")
