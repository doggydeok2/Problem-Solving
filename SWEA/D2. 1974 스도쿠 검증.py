T = int(input())
di = [0, 0, 0, 1, 1, 1, 2, 2, 2]
dj = [0, 1, 2, 0, 1, 2, 0, 1, 2]
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    checking = 1

    for i in range(9):
        checkSum1, checkMul1, checkSum2, checkMul2 = 0, 1, 0, 1
        for j in range(9):
            checkSum1 += arr[i][j]
            checkMul1 *= arr[i][j]
            checkSum2 += arr[j][i]
            checkMul2 *= arr[j][i]
        if not checkSum1 == checkSum2 == 45: checking = 0
        elif not checkMul1 == checkMul2 == 362880: checking = 0
        if not checking: break

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            checkSum1, checkMul1 = 0, 1
            for n in range(9):
                checkSum1 += arr[i + di[n]][j + dj[n]]
                checkMul1 *= arr[i + di[n]][j + dj[n]]
            if not checkSum1 == 45: checking = 0
            elif not checkMul1 == 362880: checking = 0
            if not checking: break
        if not checking: break
    print(f'#{tc} {checking}')