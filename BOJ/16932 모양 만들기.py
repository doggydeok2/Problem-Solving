import collections
import sys
rl = sys.stdin.readline


def cnt_shape(_x, _y, _n):
    cnt = 1
    visited[_x][_y] = _n
    q = collections.deque([(_x, _y)])
    while q:
        tx, ty = q.popleft()
        for k in range(4):
            nx, ny = tx + dij[k], ty + dij[k + 1]
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = _n
                q.append((nx, ny))
    return cnt


dij = [0, -1, 0, 1, 0]
N, M = map(int, rl().split())
data = [list(map(int, rl().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
nth = max_cnt = 0
cnt_arr = [0]

for i in range(N):
    for j in range(M):
        if data[i][j] == 1 and not visited[i][j]:
            nth += 1
            cnt_arr.append(cnt_shape(i, j, nth))

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            around = set()
            around_cnt = 1
            for t in range(4):
                ni, nj = i + dij[t], j + dij[t + 1]
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]:
                    around.add(visited[ni][nj])
            for n in around:
                around_cnt += cnt_arr[n]
            max_cnt = max(max_cnt, around_cnt)

print(max_cnt)
