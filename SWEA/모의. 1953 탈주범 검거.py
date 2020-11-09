dij = [0, -1, 0, 1, 0]  # 좌 상 우 하
cmd = [(0, 0, 0, 0), (1, 1, 1, 1), (0, 1, 0, 1), (1, 0, 1, 0), (0, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1), (1, 1, 0, 0)]


for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    Q = [(0, 0) for _ in range(M * N)]
    Q[0] = (R, C)
    v[R][C] = 1

    f, r = 0, 1
    while f < r:
        Y, X = Q[f][0], Q[f][1]
        for k in range(4):
            calY, calX = Y + dij[k], X + dij[k + 1]
            if 0 <= calY < N and 0 <= calX < M and not v[calY][calX]:
                if cmd[data[Y][X]][k] and cmd[data[calY][calX]][(k + 2) % 4]:
                    Q[r] = (calY, calX)
                    v[calY][calX] = v[Y][X] + 1
                    if v[calY][calX] > L: break
                    r += 1
        f += 1
    print(f'#{tc} {r}')