import heapq


N, K = map(int, input().split())
tools = list(map(int, input().split()))
tool_idx = [[] for _ in range(K + 1)]
ptrs = [0] * (K + 1)
is_in_sockets = [False] * (K + 1)
for idx, tool in enumerate(tools):
    tool_idx[tool].append(idx)

sockets = [(-(K + 1), 0) for _ in range(N)]
ans = 0
for idx, tool in enumerate(tools):
    if not is_in_sockets[tool]:
        popped = heapq.heappop(sockets)
        while -popped[0] < idx:
            popped = heapq.heappop(sockets)
        ans += 0 if popped[0] == -(K + 1) else 1
    ptrs[tool] += 1
    nxt = ptrs[tool]
    is_in_sockets[popped[1]] = False
    heapq.heappush(sockets, (-tool_idx[tool][nxt] if nxt < len(tool_idx[tool]) else -K, tool))
    is_in_sockets[tool] = True
print(ans)
