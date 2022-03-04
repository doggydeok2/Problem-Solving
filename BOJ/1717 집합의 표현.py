import sys
rl = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def find_parents(_x):
    if _x != parents[_x]:
        parents[_x] = find_parents(parents[_x])
    return parents[_x]


def union(_x, _y):
    _x = find_parents(_x)
    _y = find_parents(_y)
    if _x > _y:
        parents[_x] = _y
    else:
        parents[_y] = _x


n, m = map(int, rl().split())
parents = [i for i in range(n + 1)]
for _ in range(m):
    cmd, s, e = map(int, rl().split())
    if cmd == 0:
        union(s, e)
    else:
        print('YES' if find_parents(s) == find_parents(e) else 'NO')
