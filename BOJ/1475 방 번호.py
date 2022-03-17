N = int(input())
cnt_arr = [0] * 10
while N:
    mod = N % 10
    if mod == 9:
        cnt_arr[6] += 1
    else:
        cnt_arr[mod] += 1
    N //= 10
cnt_arr[6] -= cnt_arr[6] // 2
print(max(cnt_arr))
