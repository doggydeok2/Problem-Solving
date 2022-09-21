W, H, X, Y, P = map(int, input().split())
ans = 0
for _ in range(P):
    x, y = map(int, input().split())
    ans += X <= x <= X + W and Y <= y <= Y + H or \
           (X - x) ** 2 + (Y + H // 2 - y) ** 2 <= (H // 2) ** 2 or \
           (X + W - x) ** 2 + (Y + H // 2 - y) ** 2 <= (H // 2) ** 2
print(ans)
