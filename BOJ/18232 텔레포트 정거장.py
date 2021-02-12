import sys
input = sys.stdin.readline


N, M = map(int, input().split())
S, E = map(int, input().split())
adl = [[0], [2]] + [[i - 1, i + 1] for i in range(2, N)] + [[N - 1]]
v = [0] * (N + 1)

for _ in range(M):
    s, e = map(int, input().split())
    adl[s].append(e)
    adl[e].append(s)

q = [0] * 300001
q[0], v[S] = S, 1
ptr, target = 1, 0
while ptr != target:
    idx = q[target]
    for adj in adl[idx]:
        if not v[adj]:
            v[adj] = v[idx] + 1
            q[ptr] = adj
            ptr += 1
    if v[E]:
        print(v[E] - 1)
        break
    target += 1
