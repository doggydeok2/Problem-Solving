INF = 1e9
n, m = int(input()), int(input())
dist_arr = [[INF] * n for _ in range(n)]

for i in range(n):
    dist_arr[i][i] = 0

for _ in range(m):
    s, e, f = map(int, input().split())
    dist_arr[s - 1][e - 1] = min(f, dist_arr[s - 1][e - 1])

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist_arr[i][j] = min(dist_arr[i][j], dist_arr[i][k] + dist_arr[k][j])

for i in range(n):
    for j in range(n):
        if dist_arr[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist_arr[i][j], end=' ')
    print()
