N, M = map(int, input().split())
min_six, min_one = 1000, 1000

for _ in range(M):
    six, one = map(int, input().split())
    min_six, min_one = min(min_six, six), min(min_one, one)
print(min(min_one * N, min_six * (N // 6 + 1), min_six * (N // 6) + min_one * (N % 6)))
