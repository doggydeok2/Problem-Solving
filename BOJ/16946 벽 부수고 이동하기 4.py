import collections


def bfs(_y, _x, _v):
    q = collections.deque([(_y, _x)])
    recycle_q = collections.deque([])
    cnt = 0
    while q:
        ty, tx = q.popleft()
        cnt += 1
        for k in range(4):
            ny, nx = ty + dij[k], tx + dij[k + 1]
            if 0 <= ny < N and 0 <= nx < M and data[ny][nx] == visited[ny][nx] == 0:
                q.append((ny, nx))
                visited[ny][nx] = 1
        recycle_q.append((ty, tx))

    while recycle_q:
        ty, tx = recycle_q.popleft()
        data[ty][tx] = (cnt, _v)


dij = [0, -1, 0, 1, 0]
N, M = map(int, input().split())
data = [[int(ch) for ch in input()] for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visit_cnt = 2
ans = [''] * N

for i in range(N):
    for j in range(M):
        if data[i][j] == visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j, visit_cnt)
            visit_cnt += 1

for i in range(N):
    row = ''
    for j in range(M):
        if data[i][j] == 1:
            group_arr = []
            total = 1
            for d in range(4):
                ni, nj = i + dij[d], j + dij[d + 1]
                if 0 <= ni < N and 0 <= nj < M and data[ni][nj] != 1:
                    cnt, group = data[ni][nj]
                    if group not in group_arr:
                        group_arr.append(group)
                        total += cnt
            row += str(total % 10)
        else:
            row += '0'
    ans[i] = row

for row in ans:
    print(row)
