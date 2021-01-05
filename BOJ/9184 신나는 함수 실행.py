w = [[[0] * 21 for _ in range(21)] for __ in range(21)]
for j in range(21):
    for k in range(21):
        w[j][k][0] = w[j][0][k] = w[0][j][k] = 1

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1: break
    elif a <= 0 or b <= 0 or c <= 0:
        print('w(%i, %i, %i) = 1' % (a, b, c))
    elif a > 20 or b > 20 or c > 20:
        if not w[20][20][20]:
            for i in range(1, 21):
                for j in range(1, 21):
                    for k in range(1, 21):
                        if not w[i][j][k] and i < j < k:
                            w[i][j][k] = w[i][j][k - 1] + w[i][j - 1][k - 1] - w[i][j - 1][k]
                        elif not w[i][j][k]:
                            w[i][j][k] = w[i - 1][j - 1][k] + w[i - 1][j][k - 1] - w[i - 1][j - 1][k - 1]
        print('w(%i, %i, %i) = %i' % (a, b, c, w[20][20][20]))
    elif w[a][b][c]:
        print('w(%i, %i, %i) = %i' % (a, b, c, w[a][b][c]))
    else:
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                for k in range(1, c + 1):
                    if not w[i][j][k] and i < j < k:
                        w[i][j][k] = w[i][j][k - 1] + w[i][j - 1][k - 1] - w[i][j - 1][k]
                    elif not w[i][j][k]:
                        w[i][j][k] = w[i - 1][j][k] + w[i - 1][j - 1][k] + w[i - 1][j][k - 1] - w[i - 1][j - 1][k - 1]
        print('w(%i, %i, %i) = %i' % (a, b, c, w[a][b][c]))