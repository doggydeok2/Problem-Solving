a, b = map(int, input().split())
if b > a:
    a, b = b, a
for i in range(b, 0, -1):
    if not a % i and not b % i:
        print(i)
        break
for i in range(b, a * b + 1, b):
    if not i % a:
        print(i)
        break
