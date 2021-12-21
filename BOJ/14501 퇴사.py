N = int(input())
counseling_list = [map(int, input().split()) for _ in range(N)]
DP = [0] * (N + 1)

for i in range(N):
    DP[i] = max(DP[i - 1], DP[i])
    pe, am = counseling_list[i]
    if i + pe <= N:
        DP[i + pe] = max(DP[i + pe], DP[i] + am)

print(max(DP))
