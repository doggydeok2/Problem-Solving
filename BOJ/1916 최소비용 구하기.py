import heapq
import sys
rl = sys.stdin.readline

N, M = int(input()), int(input())
buses = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, w = map(int, rl().split())
    buses[s].append((w, e))

S, E = map(int, rl().split())
dist = [float('inf')] * (N + 1)
dist[S], pri_q = 0, [(0, S)]
while pri_q:
    pw, pe = heapq.heappop(pri_q)
    if dist[pe] < pw:
        continue
    for bw, be in buses[pe]:
        if bw + pw < dist[be]:
            dist[be] = bw + pw
            heapq.heappush(pri_q, (bw + pw, be))
print(dist[E])
