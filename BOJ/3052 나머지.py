arr = [0] * 10
cnt = 0
for t in range(10):
    N = int(input()) % 42
    chk = 1
    for i in range(cnt):
        if arr[i] == N:
            chk = 0
            break
    if chk:
        arr[cnt] = N
        cnt += 1
print(cnt)