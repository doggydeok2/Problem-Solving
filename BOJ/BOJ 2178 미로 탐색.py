def bfs():
    q = [0] * (N * M)
    q[0] = (0, 0)
    ptr, turn = 1, 0
    while ptr != turn:
        y, x = q[turn][0], q[turn][1]
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            cal_y, cal_x = y + dj, x + di
            if 0 <= cal_y < N and 0 <= cal_x < M and data[cal_y][cal_x] == '1' and not v[cal_y][cal_x]:
                q[ptr] = (cal_y, cal_x)
                ptr += 1
                v[cal_y][cal_x] = v[y][x] + 1
        turn += 1


N, M = map(int, input().split())
data = [input() for _ in range(N)]
v = [[0] * M for _ in range(N)]
v[0][0] = 1
bfs()

print(v[N - 1][M - 1])
