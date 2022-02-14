import collections


N, K = map(int, input().split())
DP = [-1] * 100001
DP[N] = 0

q = collections.deque([N])
while q:
    x = x2 = q.popleft()
    while x2 * 2 <= 100000 and DP[x2 * 2] == -1:
        q.append(x2 * 2)
        DP[x2 * 2] = DP[x2]
        x2 *= 2
    if x - 1 >= 0 and DP[x - 1] == -1:
        q.append(x - 1)
        DP[x - 1] = DP[x] + 1
    if x + 1 <= 100000 and DP[x + 1] == -1:
        q.append(x + 1)
        DP[x + 1] = DP[x] + 1
    if DP[K] != -1:
        print(DP[K])
        break
