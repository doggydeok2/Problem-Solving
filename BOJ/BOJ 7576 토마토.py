M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
q = [(0, 0)] * (M * N)
ptr, turn, days = 0, 0, 0
cnt = 0

for j in range(N):
    for i in range(M):
        if tomatoes[j][i] == 1:
            q[ptr] = (j, i)
            ptr += 1
        elif tomatoes[j][i] == 0: cnt += 1

while ptr != turn:
    y, x = q[turn][0], q[turn][1]
    if days < tomatoes[y][x]: days = tomatoes[y][x]
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        calY, calX = y + dj, x + di
        if 0 <= calY < N and 0 <= calX < M:
            if tomatoes[calY][calX] == 0:
                tomatoes[calY][calX] = tomatoes[y][x] + 1
                q[ptr] = (calY, calX)
                ptr += 1
                cnt -= 1
    turn += 1

if cnt: print(-1)
else: print(days - 1)