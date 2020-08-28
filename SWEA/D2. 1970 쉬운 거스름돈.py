value = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = [0] * 8

    for i in range(8):
        cnt[i] = N // value[i]
        N = N % value[i]
    print(f'#{tc}')
    for ea in cnt:
        print(ea, end = ' ')
    print('')