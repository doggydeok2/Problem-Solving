N = int(input())
nums = list(map(int, input().split()))
damage, nums = nums[0], sorted(nums[1:])
for num in nums:
    if damage > num:
        damage += num
    else:
        damage = 0
        break
print('Yes' if damage else 'No')
