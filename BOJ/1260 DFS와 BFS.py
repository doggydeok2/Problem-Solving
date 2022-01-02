import collections


def do_dfs(n):
    for x in adl[n]:
        if visited[x] == 0:
            visited[x] = 1
            dfs.append(x)
            do_dfs(x)


N, M, V = map(int, input().split())
visited = [0] * (N + 1)
adl = [[] for _ in range(N + 1)]
dfs, bfs = [V], [V]
visited[V] = 2

for _ in range(M):
    s, e = map(int, input().split())
    adl[s].append(e)
    adl[e].append(s)
for i in range(N + 1):
    adl[i].sort()

do_dfs(V)

q = collections.deque([V])
while q:
    idx = q.popleft()
    for i in adl[idx]:
        if visited[i] < 2:
            visited[i] += 1
            bfs.append(i)
            q.append(i)

print(*dfs)
print(*bfs)
