s = input()
cnt = [0, 0]
for ch in s:
    cnt[int(ch)] += 1

ans = ''
for ch in s:
    if ch == '0' and cnt[0]:
        ans += '0'
        cnt[0] -= 2
    elif ch == '1':
        if cnt[1]:
            cnt[1] -= 2
        else:
            ans += '1'
print(ans)
