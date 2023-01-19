n = [int(input()) for _ in range(3)]
print(min(n[0] + n[2], 2 * n[0] + n[1], n[1] + 2 * n[2]) * 2)
