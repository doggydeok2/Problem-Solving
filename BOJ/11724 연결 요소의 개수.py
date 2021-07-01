N, M = map(int, input().split())
adl = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    adl[u].append(v)
    adl[v].append(u)

q = [0] * N
ptr = tg = 0

for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        visited[i] = 1
        q[ptr] = i
        ptr += 1

        while ptr != tg:
            popped_idx = q[tg]
            for ad_idx in adl[popped_idx]:
                if not visited[ad_idx]:
                    visited[ad_idx] = 1
                    q[ptr] = ad_idx
                    ptr += 1
            tg += 1

print(cnt)