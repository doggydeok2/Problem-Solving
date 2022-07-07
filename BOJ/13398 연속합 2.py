n = int(input())
nums = list(map(int, input().split()))
DP = [[0] * n for _ in range(2)]
DP[0][0], DP[1][0] = nums[0], -float('inf')
for i in range(1, n):
    DP[0][i] = max(nums[i], DP[0][i - 1] + nums[i])
    DP[1][i] = max(DP[0][i - 1], DP[1][i - 1] + nums[i])
print(max(max(DP[0]), max(DP[1])))
