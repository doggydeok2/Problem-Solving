import collections

N = int(input())
orders = collections.deque([i for i in range(1, N + 1)])
papers = [0] + list(map(int, input().split()))
ans = []

while orders:
    tn = orders.popleft()
    ans.append(tn)
    if not orders:
        break
    paper = papers[tn]
    if paper > 0:
        for i in range(paper - 1):
            orders.append(orders.popleft())
    else:
        for i in range(-paper):
            orders.appendleft(orders.pop())
print(*ans)
