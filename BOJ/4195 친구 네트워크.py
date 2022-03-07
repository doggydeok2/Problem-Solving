import sys
rl = sys.stdin.readline
wr = sys.stdout.write


def find_group(_x):
    if friend_groups[_x] != _x:
        friend_groups[_x] = find_group(friend_groups[_x])
        cnt_arr[friend_groups[_x]] += cnt_arr[_x]
        cnt_arr[_x] = 0
    return friend_groups[_x]


def union(_x, _y):
    _x = find_group(_x)
    _y = find_group(_y)
    if _x > _y:
        cnt_arr[_y] += cnt_arr[_x]
        cnt_arr[_x] = 0
        friend_groups[_x] = _y
    else:
        cnt_arr[_x] += cnt_arr[_y]
        cnt_arr[_y] = 0
        friend_groups[_y] = _x


for tc in range(int(rl())):
    friends = dict()
    friend_groups = []
    cnt_arr = []
    F = int(rl())
    for _ in range(F):
        friendship = list(rl().split())
        for fs in friendship:
            if friends.get(fs) is None:
                idx = len(friend_groups)
                friend_groups.append(idx)
                cnt_arr.append(1)
                friends[fs] = idx
        A, B = friends[friendship[0]], friends[friendship[1]]
        if find_group(A) != find_group(B):
            union(A, B)
        wr(f'{cnt_arr[find_group(A)]}\n')
