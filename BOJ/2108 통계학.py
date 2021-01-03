import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
arr.sort()
print(int(round(sum(arr) / N, 0)))
print(arr[N // 2])
mc = c = 1
mcArr = [arr[0]]
for i in range(1, N):
    if arr[i] == arr[i - 1]:
        c += 1
        if mc < c:
            mc = c
            mcArr = []
    else:
        c = 1
    if mc == c:
        mcArr.append(arr[i])
print(mcArr[0] if len(mcArr) == 1 else mcArr[1])

print(arr[-1] - arr[0])
