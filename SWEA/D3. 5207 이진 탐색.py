def bs(n):
    global cnt
    L, R = 0, N - 1
    M = (L + R) // 2
    D = -1 if A[M] < n else 1
 
    while L <= R:
        M = (L + R) // 2
        if A[M] == n:
            cnt += 1
            return 0
        elif A[M] < n and D == -1:
            L = M + 1
            D = 1
        elif A[M] > n and D == 1:
            R = M - 1
            D = -1
        else:
            return 0
 
 
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
 
    for num in B:
        bs(num)
 
    print(f'#{tc} {cnt}')