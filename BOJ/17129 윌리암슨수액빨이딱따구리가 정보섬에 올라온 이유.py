import collections


def bfs(_x, _y):
    visited = [[0] * m for _ in range(n)]
    visited[_x][_y] = 1
    q = collections.deque([(_x, _y)])
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dij[k], ty + dij[k + 1]
            if 0 <= nx < n and 0 <= ny < m and A[nx][ny] != '1' and not visited[nx][ny]:
                visited[nx][ny] = visited[tx][ty] + 1
                q.append((nx, ny))
                if A[nx][ny] != '0':
                    return visited[tx][ty]
    return 0


dij = [0, -1, 0, 1, 0]
n, m = map(int, input().split())
A = []
sx = sy = 0
for i in range(n):
    row = input()
    start = row.find('2')
    if start != -1:
        sx, sy = i, start
    A.append(row)

result = bfs(sx, sy)
print(f'TAK\n{result}' if result else 'NIE')
