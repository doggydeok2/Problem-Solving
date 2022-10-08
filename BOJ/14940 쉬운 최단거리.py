import collections


def get_start():
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if col == 2:
                return i, j


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [['0' if data[i][j] == 0 else -1 for j in range(m)] for i in range(n)]
sx, sy = get_start()
dij = [0, -1, 0, 1, 0]

visited[sx][sy] = 0
q = collections.deque([(sx, sy)])
while q:
    tx, ty = q.popleft()
    for k in range(4):
        nx, ny = tx + dij[k], ty + dij[k + 1]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and not data[nx][ny] == 0:
            visited[nx][ny] = visited[tx][ty] + 1
            q.append((nx, ny))


for row in visited:
    print(*row)
