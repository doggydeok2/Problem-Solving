L, P = map(int, input().split())
c = list(map(int, input().split()))
print(*[n - L * P for n in c])
