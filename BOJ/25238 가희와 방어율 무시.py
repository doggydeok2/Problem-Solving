a, b = map(int, input().split())
n, r = divmod(a * (100 - b), 100)
print(1 if n < 100 else 0)