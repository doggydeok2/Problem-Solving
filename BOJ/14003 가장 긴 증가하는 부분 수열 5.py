import bisect
import sys
rl = sys.stdin.readline


N = int(rl())
nums = list(map(int, rl().split()))
LIS = []
LIS_idx = [0] * N

for i, num in enumerate(nums):
    idx = bisect.bisect_left(LIS, num)
    if idx == len(LIS):
        LIS.append(num)
    else:
        LIS[idx] = num
    LIS_idx[i] = idx

l = len(LIS)
ans = [0] * l
s = l - 1
for i in range(1, N + 1):
    if s == -1:
        break
    if LIS_idx[-i] == s:
        ans[s] = nums[-i]
        s -= 1
print(len(LIS))
print(*ans)
