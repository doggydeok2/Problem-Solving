N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.append(points[0])
ans = 0
for i in range(1, N + 1):
    ans += points[i - 1][0] * points[i][1]
    ans -= points[i][0] * points[i - 1][1]
print(round(abs(ans) / 2, 1))
