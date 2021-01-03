def perm(n, k):  # from itertools import permutations
    if n == k:
        for i in range(n):
            print(arr[i], end=' ')
        print()
    else:
        for i in range(1, N + 1):
            if not v[i]:
                arr[k] = i
                v[i] = 1
                perm(n, k + 1)
                v[i] = 0


N, M = map(int, input().split())
arr = [0] * M
v = [0] * (N + 1)
perm(M, 0)