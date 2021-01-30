def mul_matrix(arr1, arr2):
    arr = [[0] * N for _ in range(N)]
    for j in range(N):
        for i in range(N):
            for k in range(N):
                arr[j][i] = (arr[j][i] + arr1[j][k] * arr2[k][i]) % 1000
    return arr


N, B = map(int, input().split())
bit, e = 1, 0
while bit <= B:
    bit *= 2
    e += 1
exp = [0] * e
exp[0] = [list(map(int, input().split())) for _ in range(N)]

for x in range(1, e):
    exp[x] = mul_matrix(exp[x - 1], exp[x - 1])

bit = initFlag = 0
ans = [[0] * N for _ in range(N)]
for x in range(N):
    ans[x][x] = 1

while bit <= e:
    if (1 << bit) & B:
        ans = mul_matrix(ans, exp[bit])
    bit += 1

for row in ans:
    print(*row)