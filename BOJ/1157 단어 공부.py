lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
S = input()
cntArr = [0] * 26

for ch in S:
    for i in range(26):
        if lower[i] == ch or upper[i] == ch:
            cntArr[i] += 1

ch = cnt = 0
for i in range(26):
    if cntArr[i] > cnt:
        cnt = cntArr[i]
        ch = upper[i]
    elif cntArr[i] == cnt:
        ch = '?'
print(ch)