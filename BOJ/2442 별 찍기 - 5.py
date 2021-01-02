N = int(input())
for i in range(N, 0, -1):
    print(' ' * (i - 1) + '*' * (2 * (N - i) + 1))