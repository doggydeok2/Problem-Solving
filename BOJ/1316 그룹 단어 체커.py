abc = 'abcdefghijklmnopqrstuvwxyz'


def checker(s):
    cntArr = [0] * 26
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            for j in range(26):
                if s[i - 1] == abc[j]:
                    if cntArr[j]: return 0
                    else: cntArr[j] = 1
    return 1

cnt = 0
for tc in range(int(input())):
    cnt += checker(input() + '!')
print(cnt)
