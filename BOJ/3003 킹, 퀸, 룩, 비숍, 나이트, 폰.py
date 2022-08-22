corr = [1, 1, 2, 2, 2, 8]
existed = list(map(int, input().split()))
print(*[corr[i] - existed[i] for i in range(6)])
