T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}')
    for j in range(N):
        for i in range(N):
            print(arr[(N - 1) - i][j], end = '')
        print(end=' ')
        for i in range(N):
            print(arr[(N - 1) - j][(N - 1) - i], end = '')
        print(end=' ')
        for i in range(N):
            print(arr[i][(N - 1) - j], end = '')
        print()