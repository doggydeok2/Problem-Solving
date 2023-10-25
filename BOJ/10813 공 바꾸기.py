N, M = map(int, input().split())
baskets = [i for i in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    baskets[a], baskets[b] = baskets[b], baskets[a]
print(*baskets[1:])
