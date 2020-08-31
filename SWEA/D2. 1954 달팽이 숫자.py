T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    C = [[0] * N for _ in range(N)]
    cnt, cycle = 1, 0

    while N // 2 + N % 2 > 0:
        for i in range(N - 1):
            C[cycle][i + cycle] = cnt
            cnt += 1
        for i in range(N - 1):
            C[i + cycle][N - 1 + cycle] = cnt
            cnt += 1
        for i in range(N - 1):
            C[N - 1 + cycle][N - 1 + cycle - i] = cnt
            cnt += 1
        for i in range(N - 1):
            C[N - 1 + cycle - i][cycle] = cnt
            cnt += 1
        cycle += 1
        N -= 2
    if N < 0: C[cycle - 1][cycle - 1] = cnt

    print(f'#{tc}')
    for nums in C:
        for num in nums:
            print(num,end = ' ')
        print('')