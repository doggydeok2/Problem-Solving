N = int(input())
order = [0] * N
cnt = ptr = 0
while cnt < N:
    cnt += 1

    for i in range(cnt + 1):
        while order[ptr]:
            ptr += 1
            if ptr >= N:
                ptr %= N
        if i != cnt:
            ptr += 1
            if ptr >= N:
                ptr %= N

    order[ptr] = cnt
print(*order)
