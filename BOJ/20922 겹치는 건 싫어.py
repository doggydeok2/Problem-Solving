N, K = map(int, input().split())
cnt_arr = [0] * 100001
nums = list(map(int, input().split()))
l = r = max_len = 0
while l <= r < N:
    cnt_arr[nums[r]] += 1
    while cnt_arr[nums[r]] > K:
        cnt_arr[nums[l]] -= 1
        l += 1
    max_len = max(max_len, r - l + 1)
    r += 1
print(max_len)
