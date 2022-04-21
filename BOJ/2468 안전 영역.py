import collections


def find_safe_zone(_i, _n):
    visited = [[0] * _n for _ in range(_n)]
    q = collections.deque([])
    cnt = 0
    for x in range(_n):
        for y in range(_n):
            if lands[x][y] <= _i or visited[x][y]:
                continue
            cnt += 1
            q.append((x, y))
            while q:
                tx, ty = q.popleft()
                for k in range(4):
                    nx, ny = tx + dij[k], ty + dij[k + 1]
                    if 0 <= nx < N and 0 <= ny < N and lands[nx][ny] > _i and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = 1
    return cnt


N = int(input())
lands = [list(map(int, input().split())) for _ in range(N)]
dij = [0, -1, 0, 1, 0]
cnt_max = 0
for i in range(101):
    safe_land = find_safe_zone(i, N)
    if safe_land == 0:
        break
    cnt_max = max(cnt_max, safe_land)
print(cnt_max)
