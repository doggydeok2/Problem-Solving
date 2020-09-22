N = int(input())
nums = list(map(int, input().split()))
line = [0] * N

for i in range(N):
    line[i] = i + 1
    cnt = 0
    for x in range(nums[i]):
        line[i - cnt], line[i - 1 - cnt] = line[i - 1 - cnt], line[i - cnt]
        cnt += 1

for h in line:
    print(h, end = ' ')