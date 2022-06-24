from collections import deque


def check_visit_first(_y, _x):
    if not visited_first[_y][_x]:
        visited_first[_y][_x] = 1
        visit_order.append([_y + 1, _x + 1])


dij = [0, -1, 0, 1, 0]
N, M = map(int, input().split())
keys, flag = [False] * 26, False
visit_order, data, initial = [], [], []
visited_first = [[0] * M for _ in range(N)]
for i in range(N):
    row = input()
    data.append(row)
    for idx, ch in enumerate(row):
        if ch == '@':
            initial = [i, idx]
            visit_order.append([i + 1, idx + 1])
            visited_first[i][idx] = 1

while not flag:
    visited = [[0] * M for _ in range(N)]
    q = deque([initial[:]])
    while q:
        ty, tx = q.popleft()
        for k in range(4):
            ny, nx = ty + dij[k], tx + dij[k + 1]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if data[ny][nx] == '#' or 'A' <= data[ny][nx] <= 'Z' and not keys[ord(data[ny][nx]) - ord('A')]:
                    continue
                visited[ny][nx] = 1
                check_visit_first(ny, nx)
                q.append([ny, nx])
                if data[ny][nx] == '!':
                    flag = True
                    break
                if 'a' <= data[ny][nx] <= 'z':
                    keys[ord(data[ny][nx]) - ord('a')] = True
        if flag:
            break

print(len(visit_order))
for pos in visit_order:
    print(*pos)
