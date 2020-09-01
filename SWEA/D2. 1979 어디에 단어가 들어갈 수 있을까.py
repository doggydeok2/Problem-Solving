T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [0] * N
    cntArr = [0] * 15
    chkOne, length = 0, 0

    for i in range(N): arr[i] = list(map(int, input().split()))

    for y in range(N):
        cntArr[length] += 1
        length, chkOne = 0, 0
        for x in range(N):
            if arr[x][y]:
                length += 1
                chkOne = 1
            else:
                chkOne = 0
                cntArr[length] += 1
                length = 0

    for x in range(N):
        cntArr[length] += 1
        length, chkOne = 0, 0
        for y in range(N):
            if arr[x][y]:
                length += 1
                chkOne = 1
            else:
                chkOne = 0
                cntArr[length] += 1
                length = 0

    print(f'#{tc} {cntArr[K]}')