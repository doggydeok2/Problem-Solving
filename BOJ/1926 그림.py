import collections


def bfs(_x, _y):
    q = collections.deque([(_x, _y)])
    visit_cnt = 1
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dij[k], ty + dij[k + 1]
            if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] and not visited[nx][ny]:
                visit_cnt += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
    return visit_cnt


dij = [0, -1, 0, 1, 0]
n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = max_size = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] and not visited[i][j]:
            cnt += 1
            visited[i][j] = 1
            max_size = max(max_size, bfs(i, j))
print(cnt)
print(max_size)
