import sys
rl = sys.stdin.readline

N, M = map(int, rl().split())
nums = [0] + list(map(int, rl().split()))

for i in range(2, N + 1):
    nums[i] += nums[i - 1]

for i in range(M):
    s, e = map(int, rl().split())
    print(nums[e] - nums[s - 1])
