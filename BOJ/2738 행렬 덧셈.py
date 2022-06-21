N, M = map(int, input().split())
A, B = [list(map(int, input().split())) for _ in range(N)], [list(map(int, input().split())) for _ in range(N)]
for row in [[A[i][j] + B[i][j] for j in range(M)] for i in range(N)]:
    print(*row)
