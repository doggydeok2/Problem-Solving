import heapq
import sys
rl = sys.stdin.readline

N = int(rl().rstrip())
cards = []
compare_count = 0

for _ in range(N):
    heapq.heappush(cards, int(rl().rstrip()))

while len(cards) > 1:
    part_sum = heapq.heappop(cards) + heapq.heappop(cards)
    compare_count += part_sum
    heapq.heappush(cards, part_sum)

print(compare_count)
