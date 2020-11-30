N = int(input())
for i in range(1, N + 1):
    for x in range(N - i):
        print(end=' ')
    for x in range(i):
        print('*', end='')
    print()