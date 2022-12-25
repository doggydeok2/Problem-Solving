sen = input()
while sen != '#':
    cnt_arr = [0] * 26
    for ch in sen.lower():
        if 'a' <= ch <= 'z':
            cnt_arr[ord(ch) - ord('a')] = 1
    print(sum(cnt_arr))
    sen = input()
