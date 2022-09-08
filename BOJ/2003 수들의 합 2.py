import bisect


N, M = map(int, input().split())
nums = list(map(int, input().split()))
acc = [0] * N
for i in range(N):
    acc[i] = nums[i] + acc[i - 1]

ans = 0
for i in range(N):
    if acc[i] == M:
        ans += 1
        continue
    idx = bisect.bisect_left(acc, acc[i] - M, 0, i)
    if idx != i and acc[idx] == acc[i] - M:
        ans += 1
print(ans)