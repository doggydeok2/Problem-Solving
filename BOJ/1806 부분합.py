N, S = map(int, input().split())
nums = list(map(int, input().split())) + [0]
min_l = N + 1
if S <= nums[0]:
  min_l = 1
else:
  ptr_l, ptr_r, part_sum, part_len = 0, 1, nums[0] + nums[1], 2
  while ptr_l <= ptr_r < N:
    if part_sum < S:
      ptr_r += 1
      part_sum += nums[ptr_r]
      part_len += 1
    else:
      min_l = min(min_l, part_len)
      if min_l == 1:
        break
      part_sum -= nums[ptr_l]
      part_len -= 1
      ptr_l += 1

print(0 if min_l == N + 1 else min_l)
