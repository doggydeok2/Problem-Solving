N, K = map(int, input().split())
total = 1
for i in range(min(K, N - K)):
    total *= N - i
    total //= i + 1
print(total % 10007)