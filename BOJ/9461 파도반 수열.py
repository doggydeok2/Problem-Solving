l = [0, 1, 1, 1, 2, 2] + [0] * 95 


T = int(input())
for tc in range(T):
    N = int(input())
    if not l[N]:
        for i in range(6, N + 1):
            if not l[i]:
                l[i] = l[i - 1] + l[i - 5]
    print(l[N])