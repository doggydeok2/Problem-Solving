arr = [i for i in range(2 * 123457)]
arr[1] = 0
for i in range(2, 2 * 123456 + 1):
    if arr[i]:
        j = 2
        while j * i <= 2 * 123456:
            arr[j * i] = 0
            j += 1

while True:
    n = int(input())
    if not n: break
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if arr[i]: cnt += 1
    print(cnt)
