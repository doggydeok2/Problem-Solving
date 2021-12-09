import collections


N = int(input())
nums = list(map(int, input().split()))
larger_nums = [0] * N
num_dict = collections.defaultdict(list)

for i, val in enumerate(nums):
    num_dict[val].append(i)
nums = sorted(list(set(nums)))

for i, val in enumerate(nums):
    for idx in num_dict[val]:
        larger_nums[idx] = i

print(*larger_nums)