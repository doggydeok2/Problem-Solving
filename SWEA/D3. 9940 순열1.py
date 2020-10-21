def chk():
    for num in list(map(int, input().split())):
        if cntArr[num]: return 'No'
        else: cntArr[num] += 1
    return 'Yes'

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cntArr = [0] * (N + 1)

    print(f'#{tc} {chk()}')