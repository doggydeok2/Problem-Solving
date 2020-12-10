N, M = map(int, input().split())
nums = list(map(int, input().split()))
gapMin, gapMinNum = M, 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            gap = M - (nums[i] + nums[j] + nums[k])
            if gapMin > gap >= 0:
                gapMin = gap
                gapMinNum = nums[i] + nums[j] + nums[k]

print(gapMinNum)