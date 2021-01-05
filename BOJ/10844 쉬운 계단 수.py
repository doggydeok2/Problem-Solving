N = int(input())
cntArr = [0] + [1] * 9

for i in range(1, N):
    last_cntArr = cntArr
    cntArr = [0] * 10

    cntArr[1] += last_cntArr[0]
    for n in range(1, 9):
        cntArr[n - 1] += last_cntArr[n]
        cntArr[n + 1] += last_cntArr[n]
    cntArr[8] += last_cntArr[9]

print(sum(cntArr) % 1000000000)