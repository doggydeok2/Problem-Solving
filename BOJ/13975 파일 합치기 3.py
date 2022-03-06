import heapq


for t in range(int(input())):
    K = int(input())
    pages = list(map(int, input().split()))
    heapq.heapify(pages)
    fee = 0
    while len(pages) > 1:
        p1, p2 = heapq.heappop(pages), heapq.heappop(pages)
        fee += p1 + p2
        heapq.heappush(pages, p1 + p2)
    print(fee)
