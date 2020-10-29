def checking(arr):
    for h in range(arr[1], arr[2]):
        if not hUse[h]: continue
        else: return 0
    return 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    hUse = [0] * 25
    hArr = [[] for _ in range(N)]
    cnt = 0
    for i in range(N):
        s, e = map(int, input().split())
        hArr[i] = [e - s, s, e]
    hArr.sort()

    for ask in hArr:
        if checking(ask):
            cnt += 1
            for i in range(ask[1], ask[2]):
                hUse[i] = 1

    print(f'#{tc} {cnt}')
