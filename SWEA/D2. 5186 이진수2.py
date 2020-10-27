T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    ans = ''
    flag = 0
 
    print(f'#{tc}', end=' ')
    for i in range(1, 14):
        if i == 13 and N:
            print('overflow', end='')
            flag = 1
        elif N:
            if N - (1 / (2 ** i)) >= 0:
                N = N - (1 / (2 ** i))
                ans += '1'
            else:
                ans += '0'
 
    if not flag:
        for n in ans:
            print(n, end='')
    print()