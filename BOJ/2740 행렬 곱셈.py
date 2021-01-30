def cal(y, x):
    val = 0
    for i in range(M):
        val += A[y][i] * B[i][x]
    return val


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
ans = [[0] * K for _ in range(N)]

for i in range(K):
    for j in range(N):
        ans[j][i] = cal(j, i)

for li in ans:
    print(*li)