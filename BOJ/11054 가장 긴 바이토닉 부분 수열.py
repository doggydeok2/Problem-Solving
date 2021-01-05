N = int(input())
arr = list(map(int, input().split()))
lCnt, rCnt = [1] * N, [1] * N

for i in range(1, N):
    for j in range(i):
        lCnt[i] = max(lCnt[i], lCnt[j] * (arr[j] < arr[i]) + 1)
for i in range(N - 1, 0, -1):
    for j in range(N - 1, i - 1, -1):
        rCnt[i] = max(rCnt[i], rCnt[j] * (arr[j] < arr[i]) + 1)

sCnt = [lCnt[i] + rCnt[i] - 1 for i in range(N)]
print(max(sCnt))