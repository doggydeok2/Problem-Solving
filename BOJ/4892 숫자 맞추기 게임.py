i, n = 1, int(input())
while n:
    print(f'{i}. {"odd" if n % 2 else "even"} {n // 2}')
    n = int(input())
    i += 1
