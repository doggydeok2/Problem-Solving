import sys
rl = sys.stdin.readline


N, M, R = map(int, rl().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, rl().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0] * (N + 1)
visited[R] = 1
q = [R]
cnt = 2
for n in q:
    for nxt in sorted(adj[n]):
        if not visited[nxt]:
            visited[nxt] = cnt
            cnt += 1
            q.append(nxt)

for i in range(1, N + 1):
    sys.stdout.write(f'{visited[i]}\n')
