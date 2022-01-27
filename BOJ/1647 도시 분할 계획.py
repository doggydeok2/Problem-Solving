import sys
rl = sys.stdin.readline


def find_parent(_x):
    if _x != parents[_x]:
        parents[_x] = find_parent(parents[_x])
    return parents[_x]


def union(_x, _y):
    _x = find_parent(_x)
    _y = find_parent(_y)
    if _x < _y:
        parents[_y] = _x
    else:
        parents[_x] = _y


N, M = map(int, rl().split())
parents = [i for i in range(N + 1)]
roads = [(0, 0, 0) for _ in range(M)]
for i in range(M):
    s, e, w = map(int, rl().split())
    roads[i] = (w, s, e)
roads.sort()

maintenance_fee = 0
max_road = 0
for w, s, e in roads:
    if find_parent(s) != find_parent(e):
        union(s, e)
        maintenance_fee += w
        max_road = w

print(maintenance_fee - max_road)
