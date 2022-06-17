N = int(input())
data = [list(map(int, input().split())) + [1] for _ in range(N)] + [[1] * (N + 1)]
DP = [[[0, 0, 0] for _ in range(N + 1)] for __ in range(N + 1)]   # | \ --
DP[0][1][2] = 1

for i in range(N):
    for j in range(N):
        if data[i][j]:
            continue
        if data[i + 1][j] == 0:
            DP[i + 1][j][0] += DP[i][j][0] + DP[i][j][1]
        if data[i + 1][j] == data[i + 1][j + 1] == data[i][j + 1] == 0:
            DP[i + 1][j + 1][1] += DP[i][j][0] + DP[i][j][1] + DP[i][j][2]
        if data[i][j + 1] == 0:
            DP[i][j + 1][2] += DP[i][j][1] + DP[i][j][2]
print(sum(DP[N - 1][N - 1]))
