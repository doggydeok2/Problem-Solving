di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]


def dfs(y, x):
    global ans
    data[y][x] = '1'
    for k in range(4):
        cal_y, cal_x = y + dj[k], x + di[k]
        if 0 <= cal_y < N and 0 <= cal_x < N:
            if data[cal_y][cal_x] == '3':
                ans = 1
            elif data[cal_y][cal_x] == '0':
                dfs(cal_y, cal_x)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = [list(input()) for _ in range(N)]
    ans = 0

    for j in range(N):
        for i in range(N):
            if data[j][i] == '2':
                dfs(j, i)

    print(f'#{tc} {ans}')