N, M = map(int, input().split())
lands = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * M for _ in range(N)]

for i in range(M):
    DP[0][i] = DP[0][i - 1] + lands[0][i]

for i in range(1, N):
    for j in range(M):  # down
        DP[i][j] = DP[i - 1][j] + lands[i][j]
    left = DP[i][:]
    for j in range(1, M):  # left
        left[j] = max(left[j], left[j - 1] + lands[i][j])
    right = DP[i][:]
    for j in range(2, M + 1):  # right
        right[-j] = max(right[-j], right[-(j - 1)] + lands[i][-j])
    for j in range(M):
        DP[i][j] = max(DP[i][j], left[j], right[j])
print(DP[-1][-1])
