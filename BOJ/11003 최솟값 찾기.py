import collections


N, L = map(int, input().split())
nums = list(map(int, input().split()))
ans = [0] * N
q = collections.deque([])

for i, v in enumerate(nums):
    while q and nums[q[-1]] >= v:
        q.pop()
    while q and i - q[0] >= L:
        q.popleft()
    q.append(i)
    ans[i] = nums[q[0]]

print(*ans)
