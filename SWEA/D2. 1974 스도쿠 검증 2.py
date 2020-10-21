def chk():
    for j in range(9):
        cntArr = [[0] * 10 for _ in range(3)]
        for i in range(9):
           if cntArr[0][data[j][i]]: return 0
           else: cntArr[0][data[j][i]] += 1

           if cntArr[1][data[i][j]]: return 0
           else: cntArr[1][data[i][j]] += 1

           if cntArr[2][data[3 * (j // 3) + (i // 3)][(j * 3 % 9) + (i % 3)]]: return 0
           else: cntArr[2][data[3 * (j // 3) + (i // 3)][(j * 3 % 9) + (i % 3)]] += 1

    return 1


T = int(input())
for tc in range(1, T + 1):
    data = [list(map(int, input().split())) for _ in range(9)]

    print(f'#{tc} {chk()}')

