dij = [0, -1, 0, 1, 0]


N, M, K = map(int, input().split())
passage = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    passage[r - 1][c - 1] = 1

checked = [[0] * M for _ in range(N)]
cnt_max = 0

for i in range(N):
    for j in range(M):
        if passage[i][j] and not checked[i][j]:
            checked[i][j] = 1
            q = [(i, j)] * K
            q[0] = (i, j)
            ptr, tg, cnt = 1, 0, 0
            while ptr != tg:
                popped_i, popped_j = q[tg][0], q[tg][1]
                cnt += 1
                for k in range(4):
                    ti, tj = popped_i + dij[k], popped_j + dij[k + 1]
                    if 0 <= ti < N and 0 <= tj < M and not checked[ti][tj] and passage[ti][tj]:
                        checked[ti][tj] = 1
                        q[ptr] = (ti, tj)
                        ptr += 1
                tg += 1
            if cnt_max < cnt:
                cnt_max = cnt

print(cnt_max)
