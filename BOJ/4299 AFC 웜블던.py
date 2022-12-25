p, m = map(int, input().split())
print(*[-1] if ((p + m) % 2 or p < m) else [(p + m) // 2, (p - m) // 2])
