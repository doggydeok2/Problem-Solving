dij = [0, -1, 0, 1, 0]


T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    visited = [[0] * M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and field[i][j]:
                visited[i][j] = 1
                q = [(0, 0)] * (M * N)
                q[0] = (i, j)
                ptr, tg = 1, 0
                cnt += 1

                while ptr != tg:
                    popped_y, popped_x = q[tg][0], q[tg][1]
                    for k in range(4):
                        ty, tx = popped_y + dij[k], popped_x + dij[k + 1]
                        if 0 <= ty < N and 0 <= tx < M and field[ty][tx] and not visited[ty][tx]:
                            q[ptr] = (ty, tx)
                            ptr += 1
                            visited[ty][tx] = 1
                    tg += 1

    print(cnt)
