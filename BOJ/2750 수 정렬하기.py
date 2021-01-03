N = int(input())
nums = [0] * N
for i in range(N): nums[i] = int(input())

for i in range(N):
    for j in range(N - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for num in nums: print(num)