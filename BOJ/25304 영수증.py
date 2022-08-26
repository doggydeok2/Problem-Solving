X, N = int(input()), int(input())
for _ in range(N):
    n, v = map(int, input().split())
    X -= n * v
print('No' if X else 'Yes')
