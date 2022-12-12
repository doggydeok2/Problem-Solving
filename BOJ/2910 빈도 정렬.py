import collections


N, C = map(int, input().split())
nums = collections.Counter(list(map(int, input().split())))
order = sorted(nums.keys(), key=lambda x: -nums[x])
ans = []
for num in order:
    ans.extend([num] * nums[num])
print(*ans)
