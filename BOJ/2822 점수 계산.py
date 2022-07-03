nums = sorted([(int(input()), i) for i in range(1, 9)])
ans_sum, ans_idx = 0, []
for i in range(3, 8):
    ans_sum += nums[i][0]
    ans_idx.append(nums[i][1])
print(ans_sum)
print(*sorted(ans_idx))
