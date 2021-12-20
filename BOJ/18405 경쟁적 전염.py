import collections


dij = [0, 1, 0, -1, 0]
N, K = map(int, input().split())
virus_dict = collections.defaultdict(list)
data = []

for r in range(N):
    row = list(map(int, input().split()))
    data.append(row)
    for c in range(N):
        if row[c]:
            virus_dict[row[c]].append((r, c))

S, X, Y = map(int, input().split())
X, Y = X - 1, Y - 1

for t in range(S):
    q = collections.deque()
    for n in range(1, K + 1):
        for virus in virus_dict[n]:
            q.append(virus)
        virus_dict[n].clear()

    while q:
        r, c = q.popleft()
        for k in range(4):
            nr, nc = r + dij[k], c + dij[k + 1]
            if 0 <= nr < N and 0 <= nc < N and not data[nr][nc]:
                data[nr][nc] = data[r][c]
                virus_dict[data[r][c]].append((nr, nc))

    if data[X][Y]:
        break

print(data[X][Y])
