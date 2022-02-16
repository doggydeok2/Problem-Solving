import collections
import sys
rl = sys.stdin.readline

N, M, X, Y = map(int, rl().split())
adl = [set() for _ in range(N + 1)]
visit = [[0] * (N + 1) for _ in range(2)]
for _ in range(M):
    s, e = map(int, rl().split())
    adl[s].add(e)
    adl[e].add(s)

q = collections.deque([(X, 0)])
while q:
    x, mod = q.popleft()
    for nxt in adl[x]:
        another_mod = 1 if mod == 0 else 0
        if visit[another_mod][nxt] == 0 and visit[mod][x] < Y:
            visit[another_mod][nxt] = visit[mod][x] + 1
            q.append((nxt, another_mod))

mod = Y % 2
able = []
for idx, val in enumerate(visit[mod]):
    if val != 0 and val % 2 == mod:
        able.append(idx)
print(*able) if able else print(-1)
