N = int(input())
ans = 0
l = len(str(N))

for n in range(N // 2, N):
    total = n
    for i in range(l):
        total += (n // (10 ** i)) % 10
    if total == N:
        ans = n
        break

print(ans)