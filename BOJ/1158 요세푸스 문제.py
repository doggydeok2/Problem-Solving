from collections import deque


N, K = map(int, input().split())
q = deque([i for i in range(1, N + 1)])
ans = []
while q:
    for _ in range(K):
        q.append(q.popleft())
    ans.append(str(q.pop()))
print(f'<{", ".join(ans)}>')
