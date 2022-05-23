import collections


N = int(input())
nums = list(map(int, input().split()))
cnt_dict = collections.Counter(nums)
stack = []
ans = [-1] * N
for idx, val in enumerate(nums):
    while stack and cnt_dict[nums[stack[-1]]] < cnt_dict[val]:
        ans[stack.pop()] = val
    stack.append(idx)
print(*ans)
