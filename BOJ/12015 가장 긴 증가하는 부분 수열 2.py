import bisect


N = int(input())
nums = list(map(int, input().split()))
LIS = []

for num in nums:
    idx = bisect.bisect_left(LIS, num)
    if idx == len(LIS):
        LIS.append(num)
    else:
        LIS[idx] = num
print(len(LIS))
