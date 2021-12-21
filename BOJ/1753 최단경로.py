import heapq
import sys
rl = sys.stdin.readline

INF = 1e9
V, E = map(int, rl().rstrip().split())
K = int(rl().rstrip())
min_dist = [INF] * (V + 1)
edges = [[] for _ in range (V + 1)]
for _ in range(E):
    u, v, w = map(int, rl().rstrip().split())
    edges[u].append([w, v])

q = []
heapq.heappush(q, (0, K))
min_dist[K] = 0
while q:
    w, s = heapq.heappop(q)
    if min_dist[s] < w:
        continue
    for edge in edges[s]:
        tw, te = edge
        if w + tw < min_dist[te]:
            min_dist[te] = w + tw
            heapq.heappush(q, (w + tw, te))

for i in range(1, V + 1):
    print(min_dist[i] if min_dist[i] != INF else 'INF')
