T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [0] * N
    for i in range(N): arr[i] = list(map(int, input().split()))
    hit, hitMax = 0, 0
    
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            hit = 0
            for y in range(i, M + i):
                for x in range(j, M + j):
                    hit += arr[x][y]
            if hit > hitMax: hitMax = hit
    print(f'#{tc} {hitMax}')