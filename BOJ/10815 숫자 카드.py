def find_nums(_n):
    l, r = 0, N - 1
    while l <= r < N:
        m = (l + r) // 2
        if my_nums[m] > _n:
            r = m - 1
        elif my_nums[m] < _n:
            l = m + 1
        else:
            return 1
    return 0


N = int(input())
my_nums = sorted(list(map(int, input().split())))
M = int(input())
need_nums = list(map(int, input().split()))

for idx, num in enumerate(need_nums):
    need_nums[idx] = 1 if find_nums(num) else 0
print(*need_nums)
