n = int(input())
nums = [int(input())]

for i in range(1, n):
    last_nums = nums
    nums = list(map(int, input().split()))
    nums[0] += last_nums[0]
    nums[-1] += last_nums[-1]
    for j in range(1, i):
        nums[j] += max(last_nums[j - 1], last_nums[j])

print(max(nums))