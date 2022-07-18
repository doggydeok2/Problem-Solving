N, K = map(int, input().split())
satisfactions = list(map(int, input().split()))
DP = [[0] * (N + 1), [[] for _ in range(N + 1)]]

for idx, satisfaction in enumerate(satisfactions):
    DP[0][idx] = max(DP[0][idx], DP[0][idx - 1])
    if satisfaction >= K:
        DP[0][idx + 1] = DP[0][idx] + satisfaction - K
    else:
        DP[1][idx + 1].append([satisfaction, DP[0][idx]])

    for lasting in DP[1][idx]:
        ts, acc = lasting
        if ts + satisfaction >= K:
            DP[0][idx + 1] = max(DP[0][idx + 1], acc + ts + satisfaction - K)
        else:
            DP[1][idx + 1].append([ts + satisfaction, acc])

print(max(DP[0][-2], DP[0][-1]))
