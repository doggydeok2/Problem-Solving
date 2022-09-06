n = int(input())
DP = [0] * 41
DP[1] = DP[2] = 1
for i in range(3, 41):
    DP[i] = DP[i - 1] + DP[i - 2]
print(DP[n], n - 2)
