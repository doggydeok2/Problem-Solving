from collections import deque


dij = [0, -1, 1, 0, 1, 1, -1, -1, 0]
w, h = map(int, input().split())
while not w == h == 0:
    data = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    q = deque()
    cnt = 0
    for i in range(h):
        for j in range(w):
            if data[i][j] and not visited[i][j]:
                cnt += 1
                visited[i][j] = cnt
                q.append((i, j))
                while q:
                    ti, tj = q.popleft()
                    for k in range(8):
                        ni, nj = ti + dij[k], tj + dij[k + 1]
                        if 0 <= ni < h and 0 <= nj < w and data[ni][nj] and not visited[ni][nj]:
                            q.append((ni, nj))
                            visited[ni][nj] = cnt
    print(cnt)
    w, h = map(int, input().split())
