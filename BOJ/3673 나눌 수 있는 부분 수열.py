import sys
rl = sys.stdin.readline


c = int(rl())
acc_cnt_arr = [0] * 1000001
for tc in range(c):
    d, n = map(int, rl().split())
    acc_cnt_arr[0] = 1
    acc = 0
    for num in list(map(int, rl().split())):
        acc = (acc + num) % d
        acc_cnt_arr[acc] += 1

    ans = 0
    for i in range(d):
        ans += (acc_cnt_arr[i] ** 2 - acc_cnt_arr[i]) // 2 if acc_cnt_arr[i] > 1 else 0
        acc_cnt_arr[i] = 0
    print(ans)
