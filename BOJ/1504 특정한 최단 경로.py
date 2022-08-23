import heapq
import sys
rl = sys.stdin.readline


def dijkstra(_s):
    heap = [(0, _s)]
    dist = [INF] * (N + 1)
    dist[_s] = 0
    while heap:
        tc, tx = heapq.heappop(heap)
        for cost, ne in adl[tx]:
            if dist[ne] < tc + cost:
                continue
            dist[ne] = dist[tx] + cost
            heapq.heappush(heap, (dist[tx] + cost, ne))
    return dist


INF = int(1e9)
N, E = map(int, rl().split())
adl = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, rl().split())
    adl[a].append([c, b])
    adl[b].append([c, a])
v1, v2 = map(int, rl().split())
dist_s, dist_v1, dist_v2 = dijkstra(1), dijkstra(v1), dijkstra(v2)
ans = min(dist_s[v1] + dist_v1[v2] + dist_v2[N], dist_s[v2] + dist_v2[v1] + dist_v1[N])
print(ans if ans < INF else -1)
