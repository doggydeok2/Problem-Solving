M, N = map(int, input().split())
arr = [i for i in range(1000001)]
arr[1] = 0
for i in range(2, 999998):
    if arr[i]:
        j = 2
        while i * j <= 1000000:
            arr[j * i] = 0
            j += 1

for i in range(M, N + 1):
    if arr[i]: print(i)