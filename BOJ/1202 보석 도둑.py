import heapq
import sys
rl = sys.stdin.readline

N, K = map(int, rl().split())
jewels = sorted([list(map(int, rl().split())) for _ in range(N)], reverse=True)
bags = sorted([int(rl()) for _ in range(K)])
rob_able = []
robbed_max = 0
for bag in bags:
    for i in range(len(jewels)):
        if jewels[-1][0] > bag:
            break
        heapq.heappush(rob_able, -jewels.pop()[1])
    if rob_able:
        robbed_max -= heapq.heappop(rob_able)
print(robbed_max)
