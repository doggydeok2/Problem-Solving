import heapq
import sys
rl = sys.stdin.readline

N, M = map(int, rl().split())
do_first = [[] for _ in range(N + 1)]
topology = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, rl().split())
    topology[B] += 1
    do_first[A].append(B)

priority_q = []
for i in range(1, N + 1):
    if topology[i] == 0:
        heapq.heappush(priority_q, i)

did = [0] * N
ptr = 0
while priority_q:
    idx = heapq.heappop(priority_q)
    did[ptr] = idx
    ptr += 1

    for do_next in do_first[idx]:
        topology[do_next] -= 1
        if topology[do_next] == 0:
            heapq.heappush(priority_q, do_next)

print(*did)
