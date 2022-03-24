import sys
rl = sys.stdin.readline
wr = sys.stdout.write


cnt_arr_A = [0] * 102
cnt_arr_B = [0] * 102
N = int(rl())
for i in range(1, N + 1):
    A, B = map(int, rl().split())
    cnt_arr_A[A] += 1
    cnt_arr_B[B] += 1

    lp, rp = 0, 101
    l_acc = r_acc = 0
    min_sum = 0

    while True:
        while lp <= 100 and cnt_arr_A[lp] == 0:
            lp += 1
            l_acc += cnt_arr_A[lp]
        while rp > 0 and cnt_arr_B[rp] == 0:
            rp -= 1
            r_acc += cnt_arr_B[rp]

        min_sum = max(min_sum, lp + rp)
        if l_acc == r_acc == i:
            break
        if l_acc > r_acc:
            if rp > 0:
                rp -= 1
                r_acc += cnt_arr_B[rp]
        elif l_acc < r_acc:
            if lp <= 100:
                lp += 1
                l_acc += cnt_arr_A[lp]
        else:
            if rp > 0:
                rp -= 1
                r_acc += cnt_arr_B[rp]
            if lp <= 100:
                lp += 1
                l_acc += cnt_arr_A[lp]
    wr(f'{min_sum}\n')
