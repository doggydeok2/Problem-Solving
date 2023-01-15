for _ in range(int(input())):
    print(*[''.join(s[::-1]) for s in list(input().split())])
