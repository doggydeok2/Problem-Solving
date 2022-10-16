for _ in range(int(input())):
    n = input()
    print('Do-it' if n[len(n) // 2 - 1] == n[len(n) // 2] else 'Do-it-Not')
