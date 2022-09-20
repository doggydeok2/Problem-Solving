for _ in range(int(input())):
    a, b = map(int, input().split())
    n = 1
    for __ in range(b):
        n = n * a % 10
    print(n or 10)
    