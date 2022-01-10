import collections


N = int(input())
DP = [None for _ in range(10**6 + 1)]
q = collections.deque([N])

while q:
    num = q.popleft()
    if num % 3 == 0 and DP[num // 3] is None:
        DP[num // 3] = num
        q.append(num // 3)
    if num % 2 == 0 and DP[num // 2] is None:
        DP[num // 2] = num
        q.append(num // 2)
    if DP[num - 1] is None:
        DP[num - 1] = num
        q.append(num - 1)
    if DP[1] is not None:
        break

ans = [1]
while ans[-1] != N:
    ans.append(DP[ans[-1]])
ans.reverse()
print(len(ans) - 1)
print(*ans)
