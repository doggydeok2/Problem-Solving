N = ''.join(sorted([ch for ch in input()], reverse=True))
print(-1 if int(N) % 30 else N)
