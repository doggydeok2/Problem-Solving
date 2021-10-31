s = input()
ascii_arr, cnt_arr = [], []
for ch in s:
    ascii_arr.append(ord(ch))
    cnt_arr.append(1)
    for i in range(2, len(ascii_arr) + 1):
        if ascii_arr[-i] < ascii_arr[-1]:
            cnt_arr[-1] = max(cnt_arr[-i] + 1, cnt_arr[-1])

print(26 - max(cnt_arr))
