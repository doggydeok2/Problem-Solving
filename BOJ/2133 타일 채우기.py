N = int(input())
DP = [0] * 31
DP[2] = 3
for i in range(4, N + 1, 2):
    special = 0
    for j in range(0, i - 2, 2):
        special += DP[j]
    DP[i] = DP[i - 2] * 3 + special * 2 + 2
print(DP[N])
