def making_sequence(n, k, c):
    if n == k: print(*arr)
    else:
        for i in range(c, N + 1):
            arr[k] = i
            making_sequence(n, k + 1, i)


N, M = map(int, input().split())
arr = [0] * M
making_sequence(M, 0, 1)