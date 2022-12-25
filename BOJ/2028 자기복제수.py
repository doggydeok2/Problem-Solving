for _ in range(int(input())):
    N = int(input())
    l = len(str(N))
    print('NO' if (N ** 2 - N) % (10 ** l) else 'YES')
