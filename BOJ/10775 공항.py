import sys
rl = sys.stdin.readline


def find_ables(_x):
    if _x != ables[_x]:
        ables[_x] = find_ables(ables[_x])
    return ables[_x]


def simulate(_cnt):
    for i in range(_cnt):
        n = int(rl())
        able = find_ables(n)
        if able == 0:
            return i
        else:
            ables[able] = find_ables(able - 1)
    return _cnt


G, P = int(rl()), int(rl())
ables = [i for i in range(G + 1)]

print(simulate(P))
