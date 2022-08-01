from bisect import bisect_left


N = int(input())
nums = [int(input()) for _ in range(N)]

LIS_idx = [-1] * N
LIS = []
for idx, num in enumerate(nums):
    lis_i = bisect_left(LIS, num)
    if lis_i == len(LIS):
        LIS.append(num)
    else:
        LIS[lis_i] = num
    LIS_idx[idx] = lis_i
print(N - max(LIS_idx) - 1)
