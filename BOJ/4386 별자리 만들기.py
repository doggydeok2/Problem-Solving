import itertools


def find_parents(_x):
    if parents[_x] != _x:
        parents[_x] = find_parents(parents[_x])
    return parents[_x]


def union(_x, _y):
    _x = find_parents(_x)
    _y = find_parents(_y)
    if _x > _y:
        parents[_x] = _y
    else:
        parents[_y] = _x


n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]
parents = [i for i in range(n)]

distances = []
for i, j in itertools.combinations(range(n), 2):
    distances.append((((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2), i, j))
distances.sort()

min_distance = 0
for distance in distances:
    d_square, i, j = distance
    if find_parents(i) != find_parents(j):
        union(i, j)
        min_distance += d_square ** 0.5

print(round(min_distance, 2))
