N = int(input())
status = [list(map(int, input().split())) for _ in range(N)]
DP = [[[0, 0, 0] for _ in range(N)] for __ in range(N)]
status[0][0] = status[0][1] = DP[0][1][0] = 1
for i in range(N):
    for j in range(1, N):
        if i + 1 < N and j + 1 < N and status[i][j + 1] == status[i + 1][j] == status[i + 1][j + 1] == 0:
            DP[i + 1][j + 1][1] += DP[i][j][0] + DP[i][j][1] + DP[i][j][2]
        if i + 1 < N and status[i + 1][j] == 0:
            DP[i + 1][j][2] += DP[i][j][1] + DP[i][j][2]
        if j + 1 < N and status[i][j + 1] == 0:
            DP[i][j + 1][0] += DP[i][j][0] + DP[i][j][1]
print(sum(DP[N - 1][N - 1]))
