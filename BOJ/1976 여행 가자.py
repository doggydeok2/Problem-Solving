import collections


def check():
    for target in targets:
        if visited[target] == 0:
            return False
    return True


N, M = int(input()), int(input())
adj = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
targets = list(map(int, input().split()))
targets = [target - 1 for target in targets]

q = collections.deque([targets[0]])
visited[targets[0]] = 1
while q:
    tx = q.popleft()
    for i in range(N):
        if adj[tx][i] == 1 and visited[i] == 0:
            visited[i] = 1
            q.append(i)
print('YES' if check() else 'NO')
