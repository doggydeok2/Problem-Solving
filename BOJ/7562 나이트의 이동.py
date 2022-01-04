import collections


di = [-2, -1, 1, 2, -2, -1, 1, 2]
dj = [-1, -2, 2, 1, 1, 2, -2, -1]
T = int(input())
for tc in range(T):
    I = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited = [[0] * I for _ in range(I)]
    visited[sy][sx] = 1

    q = collections.deque([(sx, sy)])
    while q:
        tx, ty = q.popleft()
        for k in range(8):
            nx, ny = tx + di[k], ty + dj[k]
            if 0 <= nx < I and 0 <= ny < I and not visited[ny][nx]:
                visited[ny][nx] = visited[ty][tx] + 1
                q.append((nx, ny))
        if visited[ey][ex]:
            print(visited[ey][ex] - 1)
            break
