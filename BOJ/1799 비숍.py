def backtracking(_cnt, _y, _x, _is_odd):
    max_cnt = _cnt
    for y in range(_y, N):
        for x in range(_x if y == _y else 1 if (y + _is_odd) % 2 else 0, N, 2):
            if chess_board[y][x] == 1 and slash[y + x] == 0 and backslash[N - 1 - y + x] == 0:
                slash[y + x] = backslash[N - 1 - y + x] = 1
                max_cnt = max(max_cnt, backtracking(_cnt + 1, y, x, _is_odd))
                slash[y + x] = backslash[N - 1 - y + x] = 0
    return max_cnt


N = int(input())
chess_board = [list(map(int, input().split())) for _ in range(N)]
slash, backslash = [0] * (2 * N - 1), [0] * (2 * N - 1)
print(backtracking(0, 0, 0, 0) + backtracking(0, 0, 1, 1))
