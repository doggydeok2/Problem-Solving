N, K = map(int, input().split())
nums = list(map(int, input().split()))
acc = [-1e10] * N
acc[K - 1] = sum(nums[:K])
for i in range(K, N):
    acc[i] = acc[i - 1] + nums[i] - nums[i - K]
print(max(acc))
