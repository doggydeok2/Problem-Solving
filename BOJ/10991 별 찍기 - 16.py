N = int(input())
for i in range(1, N + 1):
    print(' ' * (N - i), end='')
    for x in range(i):
        print('*', end='')
        if not x == i: print(end=' ')
    print()