def hanoi(n, s, r, e):
    if n == 1:
        print(s, e)
    else:
        hanoi(n - 1, s, e, r)
        print(s, e)
        hanoi(n - 1, r, s, e)


N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 2, 3)