import heapq


N, M = map(int, input().split())
brightnesses = list(map(int, input().split()))
heap = []
ans = [0] * N
for idx, val in enumerate(brightnesses):
    heapq.heappush(heap, (-val, idx))
    while heap[0][1] + 2 * M - 2 < idx:
        heapq.heappop(heap)
    ans[idx] = -heap[0][0]
print(*ans[2 * M - 2:N])
