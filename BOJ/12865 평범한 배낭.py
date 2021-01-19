N, K = map(int, input().split())
vMax = [0] * (K + 1)

for i in range(N):
    W, V = map(int, input().split())
    for j in range(K, -1, -1):
        if vMax[j] and j + W <= K:
            vMax[j + W] = max(vMax[j] + V, vMax[j + W])
        if j == W:
            vMax[j] = max(vMax[j], V)

print(max(vMax))