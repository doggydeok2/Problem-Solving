N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
DP[0][0] = 1
for i in range(N):
    for j in range(N):
        n = board[i][j]
        if n == 0:
            continue
        if i + n < N:
            DP[i + n][j] += DP[i][j]
        if j + n < N:
            DP[i][j + n] += DP[i][j]
print(DP[-1][-1])
