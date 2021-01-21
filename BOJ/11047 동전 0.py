N, K = map(int, input().split())
Ai = [0] * N
cnt = 0
for i in range(N):
    Ai[i] = int(input())

for r in range(N - 1, -1, -1):
    quotient = K // Ai[r]
    cnt += quotient
    K -= Ai[r] * quotient

print(cnt)