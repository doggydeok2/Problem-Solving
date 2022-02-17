import sys
sys.setrecursionlimit(100001)
rl = sys.stdin.readline


def find_parent(_x):
    if _x != parent[_x]:
        backup_parent = parent[_x]
        parent[_x] = find_parent(parent[_x])
        diff[_x] += diff[backup_parent]
    return parent[_x]


def union(_x, _y):
    dif_x, dif_y = diff[_x], diff[_y]
    _x = find_parent(_x)
    _y = find_parent(_y)
    if _x < _y:
        parent[_y] = _x
        diff[_y] = dif_x + w - dif_y
    elif _x > _y:
        parent[_x] = _y
        diff[_x] = dif_y - w - dif_x


while True:
    N, M = map(int, rl().split())
    if N == M == 0:
        break
    parent = [i for i in range(N + 1)]
    diff = [0] * (N + 1)

    for i in range(M):
        cmd = list(rl().split())
        if cmd[0] == '!':
            a, b, w = int(cmd[1]), int(cmd[2]), int(cmd[3])
            # if a > b:
            #     a, b, w = b, a, -w
            if find_parent(a) != find_parent(b):
                union(a, b)
        else:
            a, b = int(cmd[1]), int(cmd[2])
            print(diff[b] - diff[a] if find_parent(a) == find_parent(b) else 'UNKNOWN')
