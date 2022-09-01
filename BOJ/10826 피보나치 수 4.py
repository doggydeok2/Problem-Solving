n = int(input())
DP = [0] * 10001
DP[1] = DP[2] = 1
for i in range(3, n + 1):
    DP[i] = DP[i - 1] + DP[i - 2]
print(DP[n])