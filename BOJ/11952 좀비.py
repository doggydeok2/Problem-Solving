import collections
import heapq
import sys
rl = sys.stdin.readline


N, M, K, S = map(int, rl().split())
P, Q = map(int, rl().split())
INF = Q * N

special = [-1] * (N + 1)
stolen = collections.deque([])
for _ in range(K):
    z = int(rl())
    stolen.append(z)
    special[z] = 0


adl = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, rl().split())
    adl[s].append(e)
    adl[e].append(s)

while stolen:
    tx = stolen.popleft()
    for nxt in adl[tx]:
        if special[nxt] == -1:
            special[nxt] = special[tx] + 1
            if special[nxt] < S:
                stolen.append(nxt)

total = [INF] * (N + 1)
total[1] = 0
heap = [(0, 1)]
while heap:
    tc, tx = heapq.heappop(heap)
    if tc > total[tx]:
        continue
    for nxt in adl[tx]:
        if special[nxt] == 0:
            continue
        nc = P if special[nxt] == -1 else Q
        if tc + nc < total[nxt]:
            total[nxt] = tc + nc
            heapq.heappush(heap, (tc + nc, nxt))

print(total[-1] - (P if special[-1] == -1 else Q))
