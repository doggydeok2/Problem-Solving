from collections import deque


dij = [0, -1, -1, 0, 1, 1, -1, 1, 0]
H, W, L = map(int, input().split())
words = [input() for _ in range(H)]
needs = input()
ans = 0

q = deque()
visited = [[[0] * W for _ in range(H)] for __ in range(len(needs))]
for i, word in enumerate(words):
    for j, ch in enumerate(word):
        if ch == needs[0]:
            q.append((i, j, 0))
            visited[0][i][j] = 1

while q:
    tx, ty, tn = q. popleft()
    if tn == len(needs) - 1:
        break
    nn = tn + 1
    for k in range(8):
        nx, ny = tx + dij[k], ty + dij[k + 1]
        if 0 <= nx < H and 0 <= ny < W and words[nx][ny] == needs[nn]:
            if visited[nn][nx][ny] == 0:
                q.append((nx, ny, nn))
            visited[nn][nx][ny] += visited[tn][tx][ty]
print(sum([sum(visited[-1][i]) for i in range(H)]))
