N, M = int(input()), int(input())
chars = input() + 'OO'

check_flag = False
IOI_length = 0
cnt = 0
for i in range(M + 2):
    if check_flag:
        if chars[i] == 'I' and chars[i- 1] == 'O':
            IOI_length += 1
        elif chars[i] == 'O' and chars[i - 1] == 'I':
            continue
        else:
            check_flag = False
            cnt += (IOI_length + 1 - N) if IOI_length >= N else 0
            IOI_length = 0
    if not check_flag and chars[i] == 'I':
        check_flag = True
print(cnt)
