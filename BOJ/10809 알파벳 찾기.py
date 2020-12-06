S = input()
char = 'abcdefghijklmnopqrstuvwxyz'
cntArr = [-1] * 26

for x in range(len(S)):
    for i in range(26):
        if S[x] == char[i] and cntArr[i] == -1:
            cntArr[i] = x

for i in range(26):
    print(cntArr[i], end=' ')
print()