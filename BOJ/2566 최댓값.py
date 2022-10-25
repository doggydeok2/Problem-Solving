x = y = max_n = 0
for i in range(9):
    nums = list(map(int, input().split()))
    for idx, num in enumerate(nums):
        if num > max_n:
            x, y, max_n = i + 1, idx + 1, num
print(max_n)
print(x, y)
