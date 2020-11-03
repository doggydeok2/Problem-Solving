for tc in range(1, 1 + int(input())):
    D = list(map(int, input().split()))
    
    i, ch, cnt = 1, D[1], 0
    while i < D[0]:
        pick, score = 0, 0
        if i + D[i] >= D[0]:
            break
        else:
            for x in range(i + 1, i + 1 + D[i]):
                if D[x] + x - i > score:
                    pick = x
                    score = D[x] + x - i
            i = pick
            cnt += 1
    print(f'#{tc} {cnt}')