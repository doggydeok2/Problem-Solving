import collections
import sys
rl = sys.stdin.readline


dij = [0, -1, 0, 1, 0]
T = int(rl())
for tc in range(T):
    H, W = map(int, rl().split())
    data = [rl().rstrip() for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
    cnt = 0

    q = collections.deque([])
    for i in range(H):
        for j in range(W):
            if data[i][j] == '#' and not visited[i][j]:
                cnt += 1
                visited[i][j] = 1
                q.append((i, j))
                while q:
                    ti, tj = q.popleft()
                    for k in range(4):
                        ni, nj = ti + dij[k], tj + dij[k + 1]
                        if 0 <= ni < H and 0 <= nj < W and data[ni][nj] == '#' and not visited[ni][nj]:
                            visited[ni][nj] = 1
                            q.append((ni, nj))
    print(cnt)
