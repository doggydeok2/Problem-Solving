N = int(input())
print(sum([i * (N // i) for i in range(1, N + 1)]))
