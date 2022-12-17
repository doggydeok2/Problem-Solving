def move(_x, _y, _cmd):
    if _cmd == 'D':
        return _x + 1, _y
    if _cmd == 'R':
        return _x, _y + 1
    if _cmd == 'U':
        return _x - 1, _y
    return _x, _y - 1


def get_num(_x, _y):
    slash_idx = _x + _y
    if slash_idx < N:
        initial_num = (slash_idx + 1) * slash_idx // 2 + 1
        return initial_num + (_x if slash_idx % 2 else _y)
    over_half_idx = slash_idx - (N - 1)
    initial_num = (N + 1) * N // 2 + (over_half_idx - 1) * (N - 1 + N - 1 - (over_half_idx - 1) + 1) // 2 + 1
    return initial_num + ((N - 1 - _y) if slash_idx % 2 else (N - 1 - _x))


N, K = map(int, input().split())
commands = input()
x = y = 0
ans = 1
for cmd in commands:
    x, y = move(x, y, cmd)
    ans += get_num(x, y)
print(ans)
