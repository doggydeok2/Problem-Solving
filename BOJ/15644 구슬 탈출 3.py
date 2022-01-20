import collections


def bead_escape():
    global move_flag, red_flag, blue_flag

    def check_depth(y, x, d):
        n = 0
        while True:
            n += 1
            ny, nx = y + n * dij[d], x + n * dij[d + 1]
            if board[ny][nx] != '.':
                return n

    def check_bead(y, x, cmd):
        move = check_depth(y, x, k)
        if move == 1 and board[y + dij[k]][x + dij[k + 1]] != 'O':
            return
        global move_flag
        move_flag = True

        if board[y + move * dij[k]][x + move * dij[k + 1]] == 'O':
            if cmd == 'B':
                global blue_flag
                blue_flag = True
            else:
                global red_flag
                red_flag = True
                board[y][x] = '.'
        else:
            board[y + (move - 1) * dij[k]][x + (move - 1) * dij[k + 1]], board[y][x] = \
                board[y][x], board[y + (move - 1) * dij[k]][x + (move - 1) * dij[k + 1]]

    q = collections.deque([])
    q.append((0, 0, [board_row[:] for board_row in origin_board], ''))
    q.append((0, 1, [board_row[:] for board_row in origin_board], ''))
    while q:
        cnt, t_dir, t_board, t_acc_dir = q.popleft()
        for k in range(4):
            if k % 2 == t_dir % 2:
                continue
            board = [t_board_row[:] for t_board_row in t_board]
            red_flag = blue_flag = move_flag = False
            if k == 0 or k == 1:  # left, top
                for i in range(1, N - 1):
                    for j in range(1, M - 1):
                        if board[i][j] == 'R' or board[i][j] == 'B':
                            check_bead(i, j, board[i][j])
            elif k == 2:  # right
                for i in range(1, N - 1):
                    for j in range(M - 2, 0, -1):
                        if board[i][j] == 'R' or board[i][j] == 'B':
                            check_bead(i, j, board[i][j])
            else:  # bottom
                for i in range(N - 2, 0, -1):
                    for j in range(1, M - 1):
                        if board[i][j] == 'R' or board[i][j] == 'B':
                            check_bead(i, j, board[i][j])

            if move_flag and not blue_flag:
                if red_flag:
                    return t_acc_dir + cmd[k]
                else:
                    if cnt < 9:
                        q.append((cnt + 1, (t_dir + 1) % 2, [board_row[:] for board_row in board], t_acc_dir + cmd[k]))
    return -1


dij = [0, -1, 0, 1, 0]
cmd = 'LURD'
N, M = map(int, input().split())
origin_board = [[ch for ch in input()] for _ in range(N)]
move_flag = red_flag = blue_flag = False
ans = bead_escape()
if ans != -1:
    print(len(ans))
    print(ans)
else:
    print(-1)
