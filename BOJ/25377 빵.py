INF = 1001
ans = INF
for _ in range(int(input())):
    A, B = map(int, input().split())
    ans = min(ans, B) if B - A >= 0 else ans
print(-1 if ans == INF else ans)
