import sys
rl = sys.stdin.readline


def find_group(x):
    if x != group_list[x]:
        group_list[x] = find_group(group_list[x])
    return group_list[x]


def union_group(x, y):
    x = find_group(x)
    y = find_group(y)
    if x < y:
        group_list[y] = x
    else:
        group_list[x] = y


N = int(rl().rstrip())
x_list, y_list, z_list = [], [], []
group_list = [i for i in range(N)]
minimum_cost = 0
tunnels = []

for idx in range(N):
    x, y, z = map(int, rl().rstrip().split())
    x_list.append((x, idx))
    y_list.append((y, idx))
    z_list.append((z, idx))
x_list.sort()
y_list.sort()
z_list.sort()

for i in range(N - 1):
    tunnels.append((x_list[i][0] - x_list[i + 1][0], x_list[i][1], x_list[i + 1][1]))
    tunnels.append((y_list[i][0] - y_list[i + 1][0], y_list[i][1], y_list[i + 1][1]))
    tunnels.append((z_list[i][0] - z_list[i + 1][0], z_list[i][1], z_list[i + 1][1]))
tunnels.sort()

while tunnels:
    cost, a, b = tunnels.pop()
    if find_group(a) != find_group(b):
        union_group(a, b)
        minimum_cost -= cost

print(minimum_cost)
