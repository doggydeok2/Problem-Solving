import collections


N, K = map(int, input().split())
visited = [-1] * 100001
q = collections.deque([N])

while q:
    tx = q.popleft()
    n1, n2, n3 = tx << 1, tx + 1, tx - 1
    if n1 <= 100000 and visited[n1] == -1:
        visited[n1] = tx
        q.append(n1)
    if n2 <= 100000 and visited[n2] == -1:
        visited[n2] = tx
        q.append(n2)
    if 0 <= n3 and visited[n3] == -1:
        visited[n3] = tx
        q.append(n3)
    if visited[K] != -1:
        break

pathfinder = [K]
while K != N:
    pathfinder.append(visited[K])
    K = visited[K]
print(len(pathfinder) - 1)
print(*reversed(pathfinder))
