N = int(input())
nums = [i for i in range(1, N + 1)]
f = r = 0

cnt = N
while cnt > 1:
    cnt -= 1
    r = (r + 1) % N
    nums[f] = nums[r]
    r, f = (r + 1) % N, (f + 1) % N
print(nums[f - 1])
