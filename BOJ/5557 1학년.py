N = int(input())
nums = list(map(int, input().split()))
DP = [[0] * 21 for _ in range(N - 1)]
DP[0][nums[0]] = 1
for i in range(1, N - 1):
    num = nums[i]
    for j in range(21):
        if DP[i - 1][j] == 0:
            continue
        add_num = j + num
        if add_num <= 20:
            DP[i][add_num] += DP[i - 1][j]
        subtract_num = j - num
        if subtract_num >= 0:
            DP[i][subtract_num] += DP[i - 1][j]
print(DP[-1][nums[-1]])
