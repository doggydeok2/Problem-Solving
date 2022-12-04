sc = [6, 3, 2, 1, 2]
print(*[sum([sc[i] * v for i, v in enumerate(list(map(int, input().split())))]) for _ in range(2)])
