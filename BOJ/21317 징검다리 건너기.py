N = int(input())
energies = [list(map(int, input().split())) for _ in range(N - 1)]
DP = [[1e9, 1e9] for _ in range(N + 3)]
DP[0][0] = 0
K = int(input())
for i in range(N - 1):
    DP[i + 1][0] = min(DP[i][0] + energies[i][0], DP[i + 1][0])
    DP[i + 2][0] = min(DP[i][0] + energies[i][1], DP[i + 2][0])
    DP[i + 1][1] = min(DP[i][1] + energies[i][0], DP[i + 1][1])
    DP[i + 2][1] = min(DP[i][1] + energies[i][1], DP[i + 2][1])
    DP[i + 3][1] = min(DP[i][0] + K, DP[i + 3][1])
print(min(DP[N - 1]))
