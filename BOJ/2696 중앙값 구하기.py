import heapq
import sys
rl = sys.stdin.readline
wr = sys.stdout.write


t = int(rl())
for tc in range(t):
    M = int(rl())
    wr(f'{1 + M >> 1}\n')
    sm, bg = [], []
    for i in range(0, M, 10):
        nums = list(map(int, rl().split()))
        for idx, num in enumerate(nums):
            heapq.heappush(sm, -num)
            while sm and bg and -sm[0] > bg[0]:
                heapq.heappush(sm, -heapq.heappop(bg))
                heapq.heappush(bg, -heapq.heappop(sm))
            while len(sm) - len(bg) > 1:
                heapq.heappush(bg, -heapq.heappop(sm))
            if not idx % 2:
                wr(f'{-sm[0]} ')
    if not t == tc:
        wr('\n')
