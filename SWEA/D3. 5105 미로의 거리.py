di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    q = [0] * (N ** 2)
    ptr, turn, minD = 1, 0, 10001

    for j in range(N):
        for i in range(N):
            if data[j][i] == '2':
                q[0] = [j, i]
                data[j][i] = 0

    while ptr != turn:
        y, x = q[turn][0], q[turn][1]
        for k in range(4):
            calY, calX = y + dj[k], x + di[k]
            if 0 <= calY < N and 0 <= calX < N:
                if data[calY][calX] == '3':
                    minD = data[y][x] if minD > data[y][x] else minD
                elif data[calY][calX] == '0':
                    data[calY][calX] = data[y][x] + 1
                    q[ptr] = [calY, calX]
                    ptr += 1
        turn += 1

    print(f'#{tc} {minD if minD != 10001 else 0}')