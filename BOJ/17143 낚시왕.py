import collections
import sys
rl = sys.stdin.readline

dij = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)] # U D R L
R, C, M = map(int, rl().split())
sea = [[0] * (C + 1) for _ in range(R + 1)]
sharks = collections.deque([])

for i in range(M):
    r, c, s, d, z = map(int, rl().split())

    if d == 1 or d == 2:
        s = s % (2 * (R - 1)) if R > 1 else 0
    else:
        s = s % (2 * (C - 1)) if C > 1 else 0

    sea[r][c] = (s, d, z)  # 속력, 방향, 상어 크기
    sharks.append((r, c))

size_total = 0
for j in range(1, C + 1):
    M = len(sharks)
    if M == 0:
        break

    for i in range(1, R + 1):
        if sea[i][j] != 0:
            size_total += sea[i][j][2]
            sea[i][j] = 0
            break

    new_sea = [[0] * (C + 1) for _ in range(R + 1)]
    for i in range(M):
        r, c = sharks.popleft()
        if sea[r][c] == 0:
            continue

        s, d, z = sea[r][c]
        nr, nc = r + s * dij[d][0], c + s * dij[d][1]

        while not 0 < nr <= R:
            while nr > R:
                gap = nr - R
                nr -= (2 * gap)
                d = 1 if d == 2 else 2
            while nr <= 0:
                gap = 1 - nr
                nr += (2 * gap)
                d = 1 if d == 2 else 2
        while not 0 < nc <= C:
            while nc > C:
                gap = nc - C
                nc -= (2 * gap)
                d = 3 if d == 4 else 4
            while nc <= 0:
                gap = 1 - nc
                nc += (2 * gap)
                d = 3 if d == 4 else 4

        if new_sea[nr][nc] != 0:
            if new_sea[nr][nc][2] < z:
                new_sea[nr][nc] = (s, d, z)
        else:
            new_sea[nr][nc] = (s, d, z)
            sharks.append((nr, nc))

    sea = [new_sea_row[:] for new_sea_row in new_sea]

print(size_total)
