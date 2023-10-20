N = int(input())
rows = [' ' * (N - 1 - i) + '*' * (2 * i + 1) for i in range(N)]
for row in rows:
    print(row)
for i in range(2, N + 1):
    print(rows[-i])
