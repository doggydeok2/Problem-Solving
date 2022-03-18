import sys
rl = sys.stdin.readline
wr = sys.stdout.write


nums = [1] * 1000001
nums[0] = nums[1] = 0
for i in range(2, 1000001):
    if nums[i]:
        ith = i + i
        while ith < 1000001:
            nums[ith] = 0
            ith += i

while True:
    n = int(rl())
    if n == 0:
        break
    for i in range(3, 500001, 2):
        if nums[i] and nums[n - i]:
            wr(f'{n} = {i} + {n - i}\n')
            break
