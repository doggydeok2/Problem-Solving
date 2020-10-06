T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    cntArr = [0] * 10
    MaxV, MaxN = 0, 0
     
    for num in arr: cntArr[num] += 1
    for i in range(10):
        if cntArr[i] >= MaxV:
            MaxV = cntArr[i]
            MaxN = i
    print(f'#{tc} {MaxN} {MaxV}')