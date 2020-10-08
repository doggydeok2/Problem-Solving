di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]


def bfs(y, x, color, c):
    q = [[]] * (N * N)
    q[0] = [y, x]
    ptr, turn = 1, 0
    if not c:
        while turn < ptr:
            y, x = q[turn][0], q[turn][1]
            for k in range(4):
                cal_y, cal_x = y + dj[k], x + di[k]
                if 0 <= cal_x < N and 0 <= cal_y < N and painting[cal_y][cal_x] == color and not v[cal_y][cal_x]:
                    v[cal_y][cal_x] = 1
                    q[ptr] = [cal_y, cal_x]
                    ptr += 1
            turn += 1
    else:
        while turn < ptr:
            y, x = q[turn][0], q[turn][1]
            for k in range(4):
                cal_y, cal_x = y + dj[k], x + di[k]
                if 0 <= cal_x < N and 0 <= cal_y < N and not v2[cal_y][cal_x]:
                    if color == 'B' and painting[cal_y][cal_x] == color:
                        v2[cal_y][cal_x] = 1
                        q[ptr] = [cal_y, cal_x]
                        ptr += 1
                    elif color != 'B' and painting[cal_y][cal_x] != 'B':
                        v2[cal_y][cal_x] = 1
                        q[ptr] = [cal_y, cal_x]
                        ptr += 1
            turn += 1


N = int(input())
painting = [list(input()) for _ in range(N)]
v = [[0] * N for _ in range(N)]
v2 = [[0] * N for _ in range(N)]
cnt, cntCb = 0, 0

for j in range(N):
    for i in range(N):
        if not v[j][i]:
            cnt += 1
            v[j][i] = cnt
            bfs(j, i, painting[j][i], 0)
        if not v2[j][i]:
            cntCb += 1
            v2[j][i] = cntCb
            bfs(j, i, painting[j][i], 1)

print(cnt, cntCb)