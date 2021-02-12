N = int(input())
cntArr = [[1] * 10 for _ in range(N)]
bulbs = [input() for _ in range(5)]
invalid = 0

for i in range(0, 4 * N - 1, 4):
    idx = i // 4
    if bulbs[1][i + 1] == '#' or bulbs[3][i + 1] == '#':
        invalid = 1
        break
    if bulbs[0][i] == '#':
        cntArr[idx][1] = 0
    if bulbs[0][i + 1] == '#':
        cntArr[idx][1] = 0
        cntArr[idx][4] = 0
    if bulbs[1][i] == '#':
        cntArr[idx][1] = 0
        cntArr[idx][2] = 0
        cntArr[idx][3] = 0
        cntArr[idx][7] = 0
    if bulbs[1][i + 2] == '#':
        cntArr[idx][5] = 0
        cntArr[idx][6] = 0
    if bulbs[2][i] == '#':
        cntArr[idx][1] = 0
        cntArr[idx][7] = 0
    if bulbs[2][i + 1] == '#':
        cntArr[idx][0] = 0
        cntArr[idx][1] = 0
        cntArr[idx][7] = 0
    if bulbs[3][i] == '#':
        cntArr[idx][1] = 0
        cntArr[idx][3] = 0
        cntArr[idx][4] = 0
        cntArr[idx][5] = 0
        cntArr[idx][7] = 0
        cntArr[idx][9] = 0
    if bulbs[3][i + 2] == '#':
        cntArr[idx][2] = 0
    if bulbs[4][i] == '#' or bulbs[4][i + 1] == '#':
        cntArr[idx][1] = 0
        cntArr[idx][4] = 0
        cntArr[idx][7] = 0

avg = 0
for i in range(N):
    cnt = total = 0
    for x in range(10):
        if cntArr[i][x]:
            cnt += 1
            total += x
    avg += (total / cnt) * 10 ** (N - i - 1)

print(-1 if invalid else avg)
