N = int(input())
times = list(map(int, input().split()))
Y = sum([10 * (time // 30 + 1) for time in times])
M = sum([15 * (time // 60 + 1) for time in times])
if Y < M:
    print('Y', Y)
elif Y == M:
    print('Y M', Y)
else:
    print('M', M)
