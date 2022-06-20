def print_board():
    print(f"""{gp((2, 10), 0)}{gp((2, 10), 1)}----{gp((0, 9), 0)}{gp((0, 9), 1)}----{gp((0, 8), 0)}{gp((0, 8), 1)}----{gp((0, 7), 0)}{gp((0, 7), 1)}----{gp((0, 6), 0)}{gp((0, 6), 1)}----{gp((3, 5), 0)}{gp((3, 5), 1)}
{gp((2, 10), 2)}{gp((2, 10), 3)}    {gp((0, 9), 2)}{gp((0, 9), 3)}    {gp((0, 8), 2)}{gp((0, 8), 3)}    {gp((0, 7), 2)}{gp((0, 7), 3)}    {gp((0, 6), 2)}{gp((0, 6), 3)}    {gp((3, 5), 2)}{gp((3, 5), 3)}
| \                          / |
|  \                        /  |
|   \                      /   |
|    {gp((2, 11), 0)}{gp((2, 11), 1)}                  {gp((3, 6), 0)}{gp((3, 6), 1)}    |
{gp((0, 11), 0)}{gp((0, 11), 1)}   {gp((2, 11), 2)}{gp((2, 11), 3)}                  {gp((3, 6), 2)}{gp((3, 6), 3)}   {gp((0, 4), 0)}{gp((0, 4), 1)}
{gp((0, 11), 2)}{gp((0, 11), 3)}     \                /     {gp((0, 4), 2)}{gp((0, 4), 3)}
|       \              /       |
|        \            /        |
|         {gp((2, 12), 0)}{gp((2, 12), 1)}        {gp((3, 7), 0)}{gp((3, 7), 1)}         |
|         {gp((2, 12), 2)}{gp((2, 12), 3)}        {gp((3, 7), 2)}{gp((3, 7), 3)}         |
{gp((0, 12), 0)}{gp((0, 12), 1)}          \      /          {gp((0, 3), 0)}{gp((0, 3), 1)}
{gp((0, 12), 2)}{gp((0, 12), 3)}           \    /           {gp((0, 3), 2)}{gp((0, 3), 3)}
|             \  /             |
|              {gp((1, 8), 0)}{gp((1, 8), 1)}              |
|              {gp((1, 8), 2)}{gp((1, 8), 3)}              |
|             /  \             |
{gp((0, 13), 0)}{gp((0, 13), 1)}           /    \           {gp((0, 2), 0)}{gp((0, 2), 1)}
{gp((0, 13), 2)}{gp((0, 13), 3)}          /      \          {gp((0, 2), 2)}{gp((0, 2), 3)}
|         {gp((3, 9), 0)}{gp((3, 9), 1)}        {gp((1, 9), 0)}{gp((1, 9), 1)}         |
|         {gp((3, 9), 2)}{gp((3, 9), 3)}        {gp((1, 9), 2)}{gp((1, 9), 3)}         |
|        /            \        |
|       /              \       |
{gp((0, 14), 0)}{gp((0, 14), 1)}     /                \     {gp((0, 1), 0)}{gp((0, 1), 1)}
{gp((0, 14), 2)}{gp((0, 14), 3)}   {gp((3, 10), 0)}{gp((3, 10), 1)}                  {gp((1, 10), 0)}{gp((1, 10), 1)}   {gp((0, 1), 2)}{gp((0, 1), 3)}
|    {gp((3, 10), 2)}{gp((3, 10), 3)}                  {gp((1, 10), 2)}{gp((1, 10), 3)}    |
|   /                      \   |
|  /                        \  |
| /                          \ |
{gp((0, 15), 0)}{gp((0, 15), 1)}    {gp((0, 16), 0)}{gp((0, 16), 1)}    {gp((0, 17), 0)}{gp((0, 17), 1)}    {gp((0, 18), 0)}{gp((0, 18), 1)}    {gp((0, 19), 0)}{gp((0, 19), 1)}    {gp((0, 20), 0)}{gp((0, 20), 1)}
{gp((0, 15), 2)}{gp((0, 15), 3)}----{gp((0, 16), 2)}{gp((0, 16), 3)}----{gp((0, 17), 2)}{gp((0, 17), 3)}----{gp((0, 18), 2)}{gp((0, 18), 3)}----{gp((0, 19), 2)}{gp((0, 19), 3)}----{gp((0, 20), 2)}{gp((0, 20), 3)}""")


def count_movement(_cmd):
    if len(_cmd) != 4:
        return 0
    f_cnt = 0
    for ch in _cmd:
        if ch == 'F':
            f_cnt += 1
        elif ch == 'B':
            pass
        else:
            return 0
    return f_cnt or 5


def move_piece(_piece, _n):
    initial_dir, initial_pos = piece_pos[_piece]
    moving_pieces = check_carried_piece(initial_dir, initial_pos)

    nxt_dir, nxt_pos = initial_dir, initial_pos + _n
    if initial_dir == 0:
        if nxt_pos == 5:
            nxt_dir = 3
        elif nxt_pos == 10:
            nxt_dir = 2
    elif initial_dir == 3 and nxt_pos == 8:
        nxt_dir = 1

    for piece in moving_pieces:
        if road_length[nxt_dir] < nxt_pos:
            goaled[piece] = True
            piece_pos[piece] = (-1, -1)
        else:
            piece_pos[piece] = (nxt_dir, nxt_pos)

    if not goaled[_piece]:
        kill_enemy_piece(_piece)


def check_carried_piece(_dir, _pos):
    piece = (_dir, _pos)
    pieces_list = []
    for i in range(8):
        if check_equal_position(piece, piece_pos[i]):
            pieces_list.append(i)
    return pieces_list


def check_equal_position(_piece_a, _piece_b):
    a_dir, a_pos = _piece_a
    b_dir, b_pos = _piece_b

    if a_dir == b_dir and a_pos == b_pos:
        return True

    equal_positions = equal_position[a_dir].get(a_pos)
    if equal_positions is None:
        return False
    for equal in equal_positions:
        c_dir, c_pos = equal
        if b_dir == c_dir and b_pos == c_pos:
            return True

    return False


def kill_enemy_piece(_piece):
    pieces_list = []
    s = 4 if _piece < 4 else 0
    for i in range(s, s + 4):
        if check_equal_position(piece_pos[_piece], piece_pos[i]):
            pieces_list.append(i)
    for enemy in pieces_list:
        piece_pos[enemy] = (-1, -1)


def get_piece_on_board(_pos, _piece_idx):
    x_dir, x_pos = _pos
    if _piece_idx in check_carried_piece(x_dir, x_pos):
        return pieces[_piece_idx]
    if _piece_idx + 4 in check_carried_piece(x_dir, x_pos):
        return pieces[_piece_idx + 4]
    return '.'


gp = get_piece_on_board
pieces = 'abcdABCD'
equal_position = {
    0: {
        5: [(3, 5)],
        10: [(2, 10)],
        15: [(3, 11)],
        16: [(3, 12)],
        17: [(3, 13)],
        18: [(3, 14)],
        19: [(3, 15)],
        20: [(1, 11), (2, 16), (3, 16)]
    },
    1: {
        8: [(2, 13)],
        9: [(2, 14)],
        10: [(2, 15)],
        11: [(0, 20), (2, 16), (3, 16)]
    },
    2: {
        13: [(1, 8)],
        14: [(1, 9)],
        15: [(1, 10)],
        16: [(0, 20), (1, 11), (3, 16)]
    },
    3: {
        11: [(0, 15)],
        12: [(0, 16)],
        13: [(0, 17)],
        14: [(0, 18)],
        15: [(0, 19)],
        16: [(0, 20), (1, 11), (2, 16)]
    }
}
road_length = [20, 11, 16, 16]
piece_idx = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3,
    'A': 4, 'B': 5, 'C': 6, 'D': 7
}
piece_pos = [(-1, -1) for _ in range(8)]
goaled = [False] * 8
N = int(input())
for _ in range(N):
    obj, cmd = input().split()
    obj, cmd = piece_idx.get(obj), count_movement(cmd)
    if obj is None or goaled[obj] or cmd == 0:
        continue
    if piece_pos[obj][0] == piece_pos[obj][1] == -1:
        piece_pos[obj] = (0, 0)
    move_piece(obj, cmd)
print_board()