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


N, M = map(int, input().split())
parents = [i for i in range(N + 1)]

for know in list(map(int, input().split()))[1:]:
    parents[know] = 0

parties = [list(map(int, input().split())) for _ in range(M)]
for party in parties:
    num, attendances = party[0], party[1:]
    for i in range(1, num):
        if find_parents(attendances[i - 1]) != find_parents(attendances[i]):
            union(attendances[i - 1], attendances[i])

cnt = 0
for party in parties:
    num, attendances = party[0], party[1:]
    att_parents = [find_parents(attendance) for attendance in attendances]
    cnt += att_parents.count(0) == 0
print(cnt)
