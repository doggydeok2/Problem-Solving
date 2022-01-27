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


V, E = map(int, rl().split())
parents = [i for i in range(V + 1)]
weight_total = 0

edges = [0] * E
for i in range(E):
    edges[i] = list(map(int, rl().split()))
edges.sort(key=lambda x: -x[2])

while edges:
    s, e, w = edges.pop()
    if find_parent(s) != find_parent(e):
        union(s, e)
        weight_total += w

print(weight_total)
