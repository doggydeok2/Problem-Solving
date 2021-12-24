import collections


N, K = map(int, input().split())
visited = [0] * 200001
visited[N] = 1

q = collections.deque([N])
while q:
    temp = q.popleft()
    if temp * 2 <= 200000 and not visited[temp * 2]:
        visited[temp * 2] = visited[temp] + 1
        q.append(temp * 2)
    if temp > 0 and not visited[temp - 1]:
        visited[temp - 1] = visited[temp] + 1
        q.append(temp - 1)
    if temp < 200000 and not visited[temp + 1]:
        visited[temp + 1] = visited[temp] + 1
        q.append(temp + 1)
    if visited[K]:
        break
print(visited[K] - 1)
