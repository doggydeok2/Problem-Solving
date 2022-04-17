import sys
rl = sys.stdin.readline


DP = [[0, 0, 0] for _ in range(100001)]  # 3, 1, 2
DP_sum = [0] * 100001
DP[1][1] = DP[2][2] = DP[3][0] = DP[3][1] = DP[3][2] = DP_sum[1] = DP_sum[2] = 1
DP_sum[3] = 3
mod = 1000000009

for i in range(4, 100001):
    DP[i][1] = (DP[i - 1][0] + DP[i - 1][2]) % mod
    DP[i][2] = (DP[i - 2][0] + DP[i - 2][1]) % mod
    DP[i][0] = (DP[i - 3][1] + DP[i - 3][2]) % mod
    DP_sum[i] = sum(DP[i]) % mod

for tc in range(int(rl())):
    print(DP_sum[int(rl())])
