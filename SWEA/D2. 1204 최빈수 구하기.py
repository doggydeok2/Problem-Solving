T = int(input())
for tc in range(1, T + 1):
    _ = int(input())
    cntArr = [0] * 101
    cntMax = [0, 0]

    for sc in list(map(int, input().split())):
        cntArr[sc] += 1

    for i in range(101):
        if cntMax[1] <= cntArr[i]:
            cntMax[0] = i
            cntMax[1] = cntArr[i]

    print(f'#{tc} {cntMax[0]}')