import sys
rl = sys.stdin.readline
wr = sys.stdout.write

N = int(rl())
nums = list(map(int, rl().split()))
pal_cnt_arr = [[1 - i] * N for i in range(2)]  # 0: odd, 1: even

for i in range(N - 1):
    for j in range(1, min(i + 1, N - i)):
        if nums[i - j] != nums[i + j]:
            break
        pal_cnt_arr[0][i] += 2
    for j in range(min(i + 1, N - i - 1)):
        if nums[i - j] != nums[i + 1 + j]:
            break
        pal_cnt_arr[1][i] += 2

M = int(rl())
for i in range(M):
    s, e = map(int, rl().split())
    wr('1\n' if pal_cnt_arr[(s - e) % 2][(s + e) // 2 - 1] >= (e - s + 1) else '0\n')
