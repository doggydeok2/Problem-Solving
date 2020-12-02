dij = [0, -1, 0, 1, 0]


def dfs(y, x, c, d):  # c: construct
    global maxD
    if maxD < d: maxD = d

    for k in range(4):
        n_y, n_x = y + dij[k], x + dij[k + 1]
        if 0 <= n_y < N and 0 <= n_x < N and not v[n_y][n_x]:
            if datas[y][x] > datas[n_y][n_x]:
                v[n_y][n_x] = 1
                dfs(n_y, n_x, c, d + 1)
                v[n_y][n_x] = 0
            elif not c and datas[y][x] > datas[n_y][n_x] - K:
                v[n_y][n_x] = 1
                d_temp = datas[n_y][n_x]
                datas[n_y][n_x] = datas[y][x] - 1
                dfs(n_y, n_x, c + 1, d + 1)
                v[n_y][n_x] = 0
                datas[n_y][n_x] = d_temp


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    datas = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    maxD = 1

    maxH, cnt = 0, 0
    maxHP = [(0, 0)] * 5
    for j in range(N):
        for i in range(N):
            if datas[j][i] > maxH:
                maxH = datas[j][i]
                maxHP[0] = (j, i)
                cnt = 1
            elif datas[j][i] == maxH:
                if cnt >= 5: cnt = 0
                maxHP[cnt] = (j, i)
                cnt += 1

    for t in range(cnt):
        j, i = maxHP[t]
        v[j][i] = 1
        dfs(j, i, 0, 1)
        v[j][i] = 0

    print(f'#{tc} {maxD}')
