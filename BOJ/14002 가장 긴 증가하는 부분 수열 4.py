import bisect

N = int(input())
nums = list(map(int, input().split()))
LIS, LIS_idx = [-1], [0] * N
for idx, num in enumerate(nums):
    i = bisect.bisect_left(LIS, num)
    if len(LIS) == i:
        LIS.append(num)
    else:
        LIS[i] = num
    LIS_idx[idx] = i

length = len(LIS) - 1
print(length)
ans = []
for i in range(1, N + 1):
    if length == 0:
        break
    if LIS_idx[-i] == length:
        ans.append(nums[-i])
        length -= 1
print(*ans[::-1])
