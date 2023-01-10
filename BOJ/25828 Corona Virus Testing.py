g, p, t = map(int, input().split())
a = g * p - g - t * p
print(2 if a > 0 else 1 if a < 0 else 0)
