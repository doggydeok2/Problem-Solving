n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
l, r = 0, n - 1
ans = 0
while l < r:
    if nums[l] + nums[r] > x:
        r -= 1
    else:
        ans += nums[l] + nums[r] == x
        l += 1
print(ans)
