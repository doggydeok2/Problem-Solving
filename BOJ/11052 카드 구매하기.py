N = int(input())
P = [0] + list(map(int, input().split()))

for i in range(2, N + 1):
    for j in range(i - 1, 0, -1):
        P[i] = max(P[i], P[i - j] + P[j])

print(P[N])
