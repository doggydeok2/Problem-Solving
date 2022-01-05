import collections
import sys
rl = sys.stdin.readline


def check_time():
    max_time = 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if not visited[z][y][x]:
                    return 0
                max_time = max(max_time, visited[z][y][x])
    return max_time


dijk = [1, 0, 0, -1, 0, 0, 1, 0]
M, N, H = map(int, rl().split())
tomatos = [[list(map(int, rl().split())) for i in range(N)] for j in range(H)]
visited = [[[0] * M for _ in range(N)] for __ in range(H)]

q = collections.deque([])
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomatos[k][i][j] == -1:
                visited[k][i][j] = -1
            elif tomatos[k][i][j] == 1:
                visited[k][i][j] = 1
                q.append((k, i, j))

while q:
    tk, ti, tj = q.popleft()
    for d in range(6):
        nk, ni, nj = tk + dijk[d], ti + dijk[d + 1], tj + dijk[d + 2]
        if 0 <= nk < H and 0 <= ni < N and 0 <= nj < M:
            if not visited[nk][ni][nj]:
                visited[nk][ni][nj] = visited[tk][ti][tj] + 1
                q.append((nk, ni, nj))

print(check_time() - 1)
