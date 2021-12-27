N = int(input())
edges = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            edges[i][j] = 1 if edges[i][j] or edges[i][k] and edges[k][j] else 0

for i in range(N):
    print(*edges[i])
