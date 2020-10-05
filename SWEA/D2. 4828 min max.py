T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV, minV = arr[0], arr[0]
    
    for i in range(1, N):
        if arr[i] > maxV:
            maxV = arr[i]
        if arr[i] < minV:
            minV = arr[i]
    
    print('#{} {}'.format(tc, maxV - minV))