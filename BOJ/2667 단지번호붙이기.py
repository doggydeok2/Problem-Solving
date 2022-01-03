import collections

dij = [0, -1, 0, 1, 0]
N = int(input())
data = [input() for _ in range(N)]
visited = [[0] * N for _ in range(N)]
q = collections.deque([])
complex = 0
homes = []

for i in range(N):
    for j in range(N):
        if data[i][j] == '1' and not visited[i][j]:
            complex += 1
            cnt = 1
            visited[i][j] = complex
            q.append((i, j))
            while q:
                ti, tj = q.popleft()
                for k in range(4):
                    ni, nj = ti + dij[k], tj + dij[k + 1]
                    if 0 <= ni < N and 0 <= nj < N:
                        if data[ni][nj] == '1' and visited[ni][nj] == 0:
                            visited[ni][nj] = complex
                            cnt += 1
                            q.append((ni, nj))
            homes.append(cnt)

print(complex)
for home in sorted(homes):
    print(home)
