N = int(input())
DP = [False] * 1001
DP[1] = DP[3] = DP[4] = True
for i in range(5, N + 1):
    DP[i] = not (DP[i - 4] == DP[i - 3] == DP[i - 1] is True)
print('SK' if DP[N] else 'CY')
