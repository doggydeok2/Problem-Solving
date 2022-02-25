import heapq
import sys
rl = sys.stdin.readline

n, m = int(rl()), int(rl())
buses = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, rl().split())
    buses[s].append((w, e))

S, E = map(int, rl().split())
dist = [[float('inf'), []] for _ in range(n + 1)]
dist[S][0] = 0
q = []
heapq.heappush(q, [0, S])
while q:
    w, s = heapq.heappop(q)
    if dist[s][0] < w:
        continue
    for bus in buses[s]:
        tw, te = bus
        if w + tw < dist[te][0]:
            dist[te][0] = w + tw
            dist[te][1] = dist[s][1] + [s]
            heapq.heappush(q, (w + tw, te))
dist[E][1].append(E)
print(f'{dist[E][0]}\n{len(dist[E][1])}')
print(*dist[E][1])
