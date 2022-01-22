INF = 3e9
N = int(input())
solutions = sorted(list(map(int, input().split())))
ans_sum = INF
ans_val = (0, 0, 0)

for i in range(N - 2):
    selected = solutions[i]
    l, r = i + 1, N - 1
    while l < r:
        sol_l, sol_r = solutions[l], solutions[r]
        total = selected + sol_l + sol_r
        abs_total = abs(total)
        if ans_sum > abs_total:
            ans_sum = abs_total
            ans_val = (sol_l, selected, sol_r)

        if total > 0:
            r -= 1
        else:
            l += 1

print(*sorted(ans_val))
