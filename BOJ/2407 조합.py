n, m = map(int, input().split())
total = 1

for i in range(m):
    total *= (n - i)
    total //= (i + 1)

print(total)
