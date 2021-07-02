n, k = map(int, input().split())
visited = [0] * (k + 1)
coin = [0] * n

for i in range(n):
    coin[i] = int(input())
coin = list(tuple(coin))

for i in range(n):
    visited[coin[i] if coin[i] <= k else 0] = 1
visited[0] = 0

q = coin[:]
while q:
    tx = q.pop(0)
    for val in coin:
        if 0 < tx + val <= k and not visited[tx + val]:
            visited[tx + val] = visited[tx] + 1
            if tx + val == k:
                break
            q.append(tx + val)
    if visited[k]:
        break

print(visited[k] if visited[k] else -1)
