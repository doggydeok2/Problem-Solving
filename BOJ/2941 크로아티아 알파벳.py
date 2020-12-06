S = input()
cnt = i = 0
l = len(S)
while i < l:
    if i < l - 2 and S[i] == 'd' and S[i + 1] == 'z' and S[i + 2] == '=':
        i += 3
    elif i < l - 1 and (S[i] == 'c' or S[i] == 's' or S[i] == 'z') and S[i + 1] == '=':
        i += 2
    elif i < l - 1 and (S[i] == 'c' or S[i] == 'd') and S[i + 1] == '-':
        i += 2
    elif i < l - 1 and (S[i] == 'l' or S[i] == 'n') and S[i + 1] == 'j':
        i += 2
    else:
        i += 1
    cnt += 1
print(cnt)