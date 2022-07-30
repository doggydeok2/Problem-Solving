# deque, 1220 ms
from collections import deque


for tc in range(int(input())):
    N, M, K = map(int, input().split())
    adl = [[] for _ in range(N + 1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        adl[u].append((d, c, v))

    dist = [[int(1e9)] * (M + 1) for _ in range(N + 1)]
    dist[1][0] = 0
    q = deque([(0, 0, 1)])
    while q:
        d, c, v = q.popleft()
        if d > dist[v][c]:
            continue
        for nd, nc, nv in adl[v]:
            nd, nc = d + nd, c + nc
            if nc <= M and dist[nv][nc] > nd:
                for i in range(nc, M + 1):
                    if dist[nv][i] <= nd:
                        break
                    dist[nv][i] = nd
                q.append((nd, nc, nv))
    ans = dist[-1][-1]
    print('Poor KCM' if ans == int(1e9) else ans)

# pri_q, 6280 ms
# import heapq


# for tc in range(int(input())):
#     N, M, K = map(int, input().split())
#     adl = [[] for _ in range(N + 1)]
#     for _ in range(K):
#         u, v, c, d = map(int, input().split())
#         adl[u].append((d, c, v))

#     dist = [[int(1e9)] * (M + 1) for _ in range(N + 1)]
#     dist[1][0] = 0
#     q = [(0, 0, 1)]
#     while q:
#         d, c, v = heapq.heappop(q)
#         if d > dist[v][c]:
#             continue
#         for nd, nc, nv in adl[v]:
#             nd, nc = d + nd, c + nc
#             if nc <= M and dist[nv][nc] > nd:
#                 for i in range(nc, M + 1):
#                     if dist[nv][i] <= nd:
#                         break
#                     dist[nv][i] = nd
#                 heapq.heappush(q, (nd, nc, nv))
#     ans = dist[-1][-1]
#     print('Poor KCM' if ans == int(1e9) else ans)