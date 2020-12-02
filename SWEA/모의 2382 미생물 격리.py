dij = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # 1부터 상 하 좌 우

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    bacs = [list(map(int, input().split())) for _ in range(K)]  # y, x, numbers, direction
    ables = [1] * K
    willMerge = [0] * K

    for t in range(M):
        for i in range(K):
            if not ables[i]: continue
            bac = bacs[i]
            bac[0] += dij[bac[3]][0]
            bac[1] += dij[bac[3]][1]
            if not bac[0] or not bac[1] or bac[0] == (N - 1) or bac[1] == (N - 1):
                bac[2] //= 2
                bac[3] = bac[3] + 1 if bac[3] % 2 else bac[3] - 1

        m = 0
        for i in range(K):
            if not ables[i]:
                continue
            if not bacs[i][2]:
                ables[i] = 0
                continue
            for j in range(i + 1, K):
                if ables[j] and bacs[i][0] == bacs[j][0] and bacs[i][1] == bacs[j][1] and bacs[j][2]:
                    willMerge[m] = j
                    m += 1

            cap = i
            for j in range(m):
                if bacs[cap][2] < bacs[willMerge[j]][2]:
                    cap = willMerge[j]
            bacs[i][3] = bacs[cap][3]
            for j in range(m):
                bacs[i][2] += bacs[willMerge[j]][2]
                ables[willMerge[j]] = 0
            m = 0

    s = 0
    for i in range(K):
        if ables[i]:
            s += bacs[i][2]
    print(f'#{tc} {s}')
