import collections


N, M = map(int, input().split())
nexts = [[] for _ in range(N + 1)]
topology_cnt = [0] * (N + 1)
for _ in range(M):
    orders = list(map(int, input().split()))
    for i in range(2, len(orders)):
        nexts[orders[i - 1]].append(orders[i])
        topology_cnt[orders[i]] += 1

ans = []
q = collections.deque([])
for i in range(1, N + 1):
    if topology_cnt[i] == 0:
        q.append(i)

while q:
    pop_idx = q.popleft()
    ans.append(pop_idx)
    for next in nexts[pop_idx]:
        topology_cnt[next] -= 1
        if topology_cnt[next] == 0:
            q.append(next)

if len(ans) != N:
    print(0)
else:
    for idx in ans:
        print(idx)
