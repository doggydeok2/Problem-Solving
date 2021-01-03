def checking_rnc(n, r, c):
    for x in range(9):
        if arr[r][x] == n: return 0
        if arr[x][c] == n: return 0
    return 1


def checking_block(n, by, bx):
    for y in range(by, by + 3):
        for x in range(bx, bx + 3):
            if arr[y][x] == n:
                return 0
    return 1


def backtracking(y):
    for i in range(y, 9):
        for j in range(9):
            if not arr[i][j]:
                for n in range(1, 10):
                    if not (checking_rnc(n, i, j) and checking_block(n, i // 3 * 3, j // 3 * 3)): continue
                    else:
                        arr[i][j] = n
                        if backtracking(y): return 1
                        arr[i][j] = 0
                return 0
            if j == i == 8: return 1


arr = [list(map(int, input().split())) for _ in range(9)]
backtracking(0)
for row in arr:
    print(*row)
