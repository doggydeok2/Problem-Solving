import collections


dij = [0, 1, 0, -1, 0]
M, N = map(int, input().split())
data = [list(input()) for _ in range(N)]
visited = [[10000] * M for _ in range(N)]
visited[0][0] = 0

q = collections.deque([(0, 0)])
while q:
    ty, tx = q.popleft()
    for k in range(4):
        ny, nx = ty + dij[k], tx + dij[k + 1]
        if 0 <= ny < N and 0 <= nx < M:
            crashed = visited[ty][tx] + (data[ny][nx] == '1')
            if visited[ny][nx] > crashed:
                q.append((ny, nx))
                visited[ny][nx] = crashed
print(visited[N - 1][M - 1])
