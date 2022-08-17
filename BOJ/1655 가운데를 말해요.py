import heapq
import sys
rl = sys.stdin.readline

N = int(rl())
smq, biq = [12345], [12345]

for i in range(N):
    n = int(rl())
    if biq[0] < n:
        heapq.heappush(biq, n)
        while len(biq) - len(smq) > 0:
            heapq.heappush(smq, -heapq.heappop(biq))
    else:
        heapq.heappush(smq, -n)
        while len(smq) - len(biq) > 1:
            heapq.heappush(biq, -heapq.heappop(smq))
    print(-smq[0])
