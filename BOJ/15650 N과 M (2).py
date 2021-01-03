def comb(n, k, c):  # from itertools import combinations
    if n == k:
        for i in range(1, N + 1):
            if v[i]: print(i, end=' ')
        print()
    else:
        for i in range(c + 1, N + 1):
            if not v[i]:
                v[i] = 1
                comb(n, k + 1, i)
                v[i] = 0


N, M = map(int, input().split())
v = [0] * (N + 1)
comb(M, 0, 0)

