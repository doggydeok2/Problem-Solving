N = int(input())
nums = sorted(list(map(int, input().split())))
ans = 0
for idx, num in enumerate(nums):
    l, r = 0, N - 1
    while l < r:
        r -= r == idx
        l += l == idx
        if l >= r:
            break
        temp = nums[l] + nums[r]
        if num == temp:
            ans += 1
            break
        elif num < temp:
            r -= 1
        else:
            l += 1

print(ans)
