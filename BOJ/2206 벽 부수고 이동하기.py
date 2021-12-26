import collections


dij = [0, -1, 0, 1, 0]
N, M = map(int, input().split())
data = [input() for _ in range(N)]
visited, visited_b = [[0] * M for _ in range(N)], [[0] * M for _ in range(N)]
visited[0][0] = visited_b[0][0] = 1

q = collections.deque([[0, 0, 0]])
while q:
    y, x, b = q.popleft()
    for k in range(4):
        ty, tx = y + dij[k], x + dij[k + 1]
        if 0 <= ty < N and 0 <= tx < M:
            if b == 1 and data[ty][tx] == '0' and not visited_b[ty][tx]:
                visited_b[ty][tx] = visited_b[y][x] + 1
                q.append([ty, tx, b])
            elif b == 0 and data[ty][tx] == '1' and not visited_b[ty][tx]:
                visited_b[ty][tx] = visited[y][x] + 1
                q.append([ty, tx, b + 1])
            elif b == 0 and data[ty][tx] == '0' and not visited[ty][tx]:
                if not visited_b[ty][tx]:
                    visited_b[ty][tx] = visited_b[y][x] + 1
                visited[ty][tx] = visited[y][x] + 1
                q.append([ty, tx, b])
            # else do nothing

min_distance = min(visited[N - 1][M - 1] or 1e9, visited_b[N - 1][M - 1] or 1e9)
print(min_distance if min_distance != 1e9 else -1)
