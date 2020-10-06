T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    maxSum, minSum = M, 10000 * M # 문제에서 주어진 최소, 최대
    total = 0
 
    for i in range(N - M + 1):
        total = 0
        for j in range(i, i + M): total += arr[j]
        if maxSum < total: maxSum = total
        if minSum > total: minSum = total
    print(f'#{tc} {maxSum - minSum}')
