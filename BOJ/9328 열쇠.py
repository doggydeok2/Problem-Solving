import collections
import sys
rl = sys.stdin.readline


def set_keys(_str):
    return set() if _str == '0' else set(list(_str))


def check_movable(_ch):
    return _ch in '.$' or 'a' <= _ch <= 'z' or _ch.lower() in keys


T = int(rl())
dij = [0, -1, 0, 1, 0]
q = collections.deque([])
for tc in range(T):
    h, w = map(int, rl().split())
    stage = [rl().rstrip() for _ in range(h)]
    keys = set_keys(rl().rstrip())
    visited = [[-1] * w for _ in range(h)]
    key_cnt = docs_max = 0
    while True:
        key_cnt = len(keys)
        docs = 0
        for i in range(w):
            if check_movable(stage[0][i]):
                q.append((0, i))
                visited[0][i] = key_cnt
            if check_movable(stage[h - 1][i]):
                q.append((h - 1, i))
                visited[h - 1][i] = key_cnt
        for i in range(1, h - 1):
            if check_movable(stage[i][0]):
                q.append((i, 0))
                visited[i][0] = key_cnt
            if check_movable(stage[i][w - 1]):
                q.append((i, w - 1))
                visited[i][w - 1] = key_cnt
        while q:
            th, tw = q.popleft()
            docs += stage[th][tw] == '$'
            if 'a' <= stage[th][tw] <= 'z':
                keys.add(stage[th][tw])
            for k in range(4):
                nh, nw = th + dij[k], tw + dij[k + 1]
                if 0 <= nh < h and 0 <= nw < w and visited[nh][nw] != key_cnt and check_movable(stage[nh][nw]):
                    visited[nh][nw] = key_cnt
                    q.append((nh, nw))
        docs_max = max(docs, docs_max)
        if key_cnt == len(keys):
            break
    print(docs_max)
