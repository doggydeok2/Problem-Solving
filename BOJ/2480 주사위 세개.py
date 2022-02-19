nums = sorted(list(map(int, input().split())), reverse=True)
if nums[0] == nums[1] == nums[2]:
    print(10000 + nums[0] * 1000)
elif nums[0] == nums[1] or nums[1] == nums[2]:
    print(1000 + nums[1] * 100)
else:
    print(nums[0] * 100)
