from collections import deque


F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)
visited[S] = 1
q = deque([S])
while q:
    floor = q.popleft()
    up, down = floor + U, floor - D
    if up <= F and not visited[up]:
        visited[up] = visited[floor] + 1
        q.append(up)
    if 0 < down and not visited[down]:
        visited[down] = visited[floor] + 1
        q.append(down)
print(visited[G] - 1 if visited[G] else 'use the stairs')
