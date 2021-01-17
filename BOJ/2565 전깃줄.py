N = int(input())
arr = [0] * 502
cntArr = [0] * 502

for i in range(N):
    s, e = map(int, input().split())
    arr[s] = e

for i in range(1, 501):
    prev = 0
    if arr[i]:
        for j in range(1, i):
            prev = max(cntArr[j] * (arr[i] > arr[j] > i or (i >= arr[j] > 0 and arr[i] > arr[j])), prev)
        cntArr[i] = prev + 1

print(N - max(cntArr))
