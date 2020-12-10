N, M = map(int, input().split())
chess = [input() for _ in range(N)]

cntMin = 64
for y in range(N - 7):
    for x in range(M - 7):
        cnt = 0
        for i in range(y, y + 8):
            for j in range(x, x + 8):
                if (j + i) % 2 and chess[i][j] == 'W' or not (j + i) % 2 and chess[i][j] == 'B':
                    debug = 1
                    cnt += 1
        cnt = min(cnt, 64 - cnt)
        if cntMin > cnt: cntMin = cnt

print(cntMin)
