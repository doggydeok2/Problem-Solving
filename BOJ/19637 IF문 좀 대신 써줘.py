import sys
rl = sys.stdin.readline
wr = sys.stdout.write


def get_title(_value):
    l, m, r = 0, 0, len(values) - 1
    while l <= r:
        m = (l + r) // 2
        if values[m] == _value:
            return titles[m]
        elif values[m] < _value:
            l = m + 1
        else:
            r = m - 1
    return titles[l]


N, M = map(int, rl().split())

titles, values = [], []
for _ in range(N):
    title, value = rl().split()
    value = int(value)
    if values and value == values[-1]:
        continue
    titles.append(title)
    values.append(value)

for _ in range(M):
    wr(get_title(int(rl())) + "\n")
