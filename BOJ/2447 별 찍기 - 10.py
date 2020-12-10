def star(n, y, x):
    if n == 1: pass
    else:
        nx = n // 3
        for j in range(3):
            for i in range(3):
                if j == i == 1:
                    for a in range(nx):
                        for b in range(nx):
                            arr[y + nx + a][x + nx + b] = ' '
                else: star(nx, y + nx * j, x + nx * i)


N = int(input())
arr = [['*'] * N for _ in range(N)]
for k in range(2, 8):
    if 3 ** k == N: k = N

star(N, 0, 0)
for j in range(N):
    for i in range(N):
        print(arr[j][i], end='')
    print()