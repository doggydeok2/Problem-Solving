import sys
rl = sys.stdin.readline


N, M = map(int, rl().split())
table = [list(map(int, rl().split())) for _ in range(N)]
two_dim_acc = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        two_dim_acc[i][j] = two_dim_acc[i - 1][j] + two_dim_acc[i][j - 1] - two_dim_acc[i - 1][j - 1] + table[i - 1][j - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, rl().split())
    print(two_dim_acc[x2][y2] - two_dim_acc[x2][y1 - 1] - two_dim_acc[x1 - 1][y2] + two_dim_acc[x1 - 1][y1 - 1])
