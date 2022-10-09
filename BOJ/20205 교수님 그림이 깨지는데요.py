N, K = map(int, input().split())
ans = []
for i in range(N):
    row = list(map(int, input().split()))
    ans.append([row[x // K] for x in range(N * K)])
for row in ans:
    for _ in range(K):
        print(*row)
