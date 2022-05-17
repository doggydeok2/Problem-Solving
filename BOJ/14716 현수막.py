import collections


def bfs(_x, _y, _c):
    q = collections.deque([(_x, _y)])
    while q:
        tx, ty = q.popleft()
        for k in range(8):
            nx, ny = tx + dij[k], ty + dij[k + 1]
            if 0 <= nx < M and 0 <= ny < N and data[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = _c
                q.append((nx, ny))


M, N = map(int, input().split())
dij = [0, -1, 0, 1, 1, -1, -1, 1, 0]
data = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

cnt = 0
for i in range(M):
    for j in range(N):
        if data[i][j] and not visited[i][j]:
            cnt += 1
            bfs(i, j, cnt)
print(cnt)
