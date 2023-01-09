n = int(input())
while n:
    print(sorted([input() for _ in range(n)], key=lambda x: x.lower())[0])
    n = int(input())
