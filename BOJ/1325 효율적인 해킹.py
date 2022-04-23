import collections
import sys
rl = sys.stdin.readline


N, M = map(int, rl().split())
adl = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, rl().split())
    adl[B].append(A)

ans_cnt, ans = 0, []
for i in range(1, N + 1):
    q = collections.deque([i])
    visited = [False] * (N + 1)
    visited[i] = True
    cnt = 0
    while q:
        p_idx = q.popleft()
        cnt += 1
        for n_idx in adl[p_idx]:
            if visited[n_idx]:
                continue
            q.append(n_idx)
            visited[n_idx] = True
    if cnt > ans_cnt:
        ans_cnt = cnt
        ans = [i]
    elif cnt == ans_cnt:
        ans.append(i)
    # else do nothing
print(*ans)
