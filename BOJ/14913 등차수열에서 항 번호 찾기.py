a, d, k = map(int, input().split())
print('X' if (k - a) % d or (d > 0 and k < a or d < 0 and k > a) else 1 + (k - a) // d)
