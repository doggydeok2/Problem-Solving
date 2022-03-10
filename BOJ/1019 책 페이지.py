N = int(input())
cnt_arr = [0] * 10
for i in range(11):
    exp = 10 ** i
    n, d = divmod(N, exp)
    if d == N:
        break
    rest, check_point = divmod(n, 10)
    cnt_arr[0] += (rest - 1) * exp + d + 1 if check_point == 0 else rest * exp
    for x in range(1, 10):
        if x > check_point:
            cnt_arr[x] += rest * exp
        elif x == check_point:
            cnt_arr[x] += rest * exp + (d + 1)
        else:
            cnt_arr[x] += (rest + 1) * exp
print(*cnt_arr)
