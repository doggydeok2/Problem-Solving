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


n, m = map(int, input().split())
parents = [i for i in range(n)]
ans = 0
for i in range(m):
    x, y = map(int, input().split())
    if find_parents(x) != find_parents(y):
        union(x, y)
    else:
        ans = i + 1
        break
print(ans)
