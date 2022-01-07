INF = int(1e9)
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
roads = [[INF] * n for _ in range(n)]
for i in range(n):
    roads[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    a, b = a - 1, b - 1
    roads[a][b] = roads[b][a] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            roads[i][j] = min(roads[i][j], roads[i][k] + roads[k][j])

print(max(sum([items[j] * (roads[i][j] <= m) for j in range(n)]) for i in range(n)))
