# Read input
n = int(input())
sequence = list(map(int, input().split()))


def average_nums(n, sequence):
    result = []
    avg = sum(sequence) / len(sequence)

    for i in range(n):
        if sequence[i] == avg:
            result.append(i + 1)
    print(len(result))
    print(*result)
average_nums(n, sequence)