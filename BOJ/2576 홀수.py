s, m = 0, 101
for _ in range(7):
    n = int(input())
    if n % 2:
        s += n
        m = min(m, n)
print(-1 if s == 0 else f'{s}\n{m}')
