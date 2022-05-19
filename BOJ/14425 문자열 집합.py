N, M = map(int, input().split())
S = {}
for _ in range(N):
    S[input()] = 1
print(sum([1 if S.get(input()) else 0 for _ in range(M)]))
