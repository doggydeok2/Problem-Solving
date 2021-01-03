def perm_repeat(n, k):  # from itertools import product
    if n == k:
        for n in arr:
            print(n, end=' ')
        print()
    else:
        for i in range(1, N + 1):
            arr[k] = i
            perm_repeat(n, k + 1)


N, M = map(int, input().split())
arr = [0] * M
perm_repeat(M, 0)