T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    total = 0

    ps = list(map(int, input().split()))
    maxP = ps[-1]
    for i in range(N - 2, -1, -1):
        if maxP > ps[i]: total += maxP - ps[i]
        else: maxP = ps[i]

    print(f'#{tc} {total}')