dij = [0, -1, 0, 1, 0]


def bfs(y, x, cmd):
    q = [(y, x)]
    pop_y = pop_x = 0
    if cmd:
        v[y][x] = 1
        edges = []
        while q:
            pop_y, pop_x = q.pop(0)
            flag = 1
            for k in range(4):
                ty, tx = pop_y + dij[k], pop_x + dij[k + 1]
                if 0 <= ty < h and 0 <= tx < w and data[ty][tx] == 'L' and not v[ty][tx]:
                    v[ty][tx] = v[pop_y][pop_x] + 1
                    q.append((ty, tx))
                    flag = 0
            if flag:
                edges.append((pop_y, pop_x))
    else:
        cal_v = [[0] * w for _ in range(h)]
        cal_v[y][x] = 1
        while q:
            pop_y, pop_x = q.pop(0)
            for k in range(4):
                ty, tx = pop_y + dij[k], pop_x + dij[k + 1]
                if 0 <= ty < h and 0 <= tx < w and data[ty][tx] == 'L' and not cal_v[ty][tx]:
                    cal_v[ty][tx] = cal_v[pop_y][pop_x] + 1
                    q.append((ty, tx))

    return edges if cmd else cal_v[pop_y][pop_x] - 1


h, w = map(int, input().split())
data = [input() for _ in range(h)]
v = [[0] * w for _ in range(h)]
maxD = 0

for j in range(h):
    for i in range(w):
        if data[j][i] == 'L' and not v[j][i]:
            edgeList = bfs(j, i, 1)
            for edge in edgeList:
                thisD = bfs(edge[0], edge[1], 0)
                if maxD < thisD:
                    maxD = thisD
print(maxD)
