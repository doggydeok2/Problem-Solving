N, M = int(input()), int(input())
x = list(map(int, input().split()))
max_gap = 0
for i in range(1, M):
    max_gap = max(max_gap, x[i] - x[i - 1])
print(max(x[0], N - x[-1], max_gap // 2 + max_gap % 2))
