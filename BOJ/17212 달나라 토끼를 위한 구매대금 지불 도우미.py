N = int(input())
DP = [0, 1, 1, 2, 2, 1, 2, 1] + [0] * N
for i in range(8, N + 1):
    DP[i] = min(DP[i - 1], DP[i - 2], DP[i - 5], DP[i - 7]) + 1
print(DP[N])
