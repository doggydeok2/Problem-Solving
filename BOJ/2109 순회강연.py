import heapq
import sys
rl = sys.stdin.readline


n = int(rl())
lectures = [(0, 0) for _ in range(n)]
for i in range(n):
    pay, day = map(int, rl().split())
    lectures[i] = (day, -pay)
heapq.heapify(lectures)

gonna = []
while lectures:
    day, pay = heapq.heappop(lectures)
    if len(gonna) < day:
        heapq.heappush(gonna, -pay)
    elif -pay > gonna[0]:
        heapq.heappop(gonna)
        heapq.heappush(gonna, -pay)
print(sum(gonna))
