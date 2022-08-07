import collections


A, K = map(int, input().split())
DP = [-1] * 1000001
DP[A] = 0

q = collections.deque([A])
while q:
    n = q.popleft()
    if n == K:
        print(DP[n])
        break
    if n < 1000000 and DP[n + 1] == -1:
        DP[n + 1] = DP[n] + 1
        q.append(n + 1)
    if n <= 500000 and DP[n * 2] == -1:
        DP[n * 2] = DP[n] + 1
        q.append(n * 2)
