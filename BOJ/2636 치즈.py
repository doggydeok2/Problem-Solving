import collections
dij = [0, 1, 0, -1, 0]


def bfs(y, x, t):
    q = collections.deque([[y, x]])

    while q:
        ty, tx = q.popleft()
        for m in range(4):
            cal_y, cal_x = ty + dij[m], tx + dij[m + 1]
            if 0 <= cal_y < H and 0 <= cal_x < W and not data[cal_y][cal_x] and not v[cal_y][cal_x]:
                v[cal_y][cal_x] = t
                q.append([cal_y, cal_x])


H, W = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(H)]
v = [[0] * W for _ in range(H)]
h, cnt, cnt_last = 1, 1, 0
v[0][0] = 1
bfs(0, 0, 1)

while cnt:
    h += 1
    cnt = 0
    for j in range(1, H - 1):
        for i in range(1, W - 1):
            if not v[j][i]:
                if data[j][i]:
                    for k in range(4):
                        tj, ti = j + dij[k], i + dij[k + 1]
                        if not data[tj][ti] and v[tj][ti] == h - 1:
                            v[j][i] = h
                            cnt += data[j][i]
                            data[j][i] = 0
                            bfs(j, i, h)
                else:
                    for k in range(4):
                        tj, ti = j + dij[k], i + dij[k + 1]
                        if v[tj][ti] == h:
                            v[j][i] = h
                            bfs(j, i, h)
    if cnt:
        cnt_last = cnt

print(h - 2)
print(cnt_last)