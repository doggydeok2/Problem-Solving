K = int(input())
DnL = [list(map(int, input().split())) for _ in range(6)]
DnL *= 2
W, H, ans = 0, 0, 0

for i in range(6):
    if DnL[i][0] == 1: H += DnL[i][1]
    elif DnL[i][0] == 3: W += DnL[i][1]

for i in range(2, 8):
    if DnL[i][0] == DnL[i - 2][0] and DnL[i + 1][0] == DnL[i - 1][0]:
        ans = K * ((W * H) - (DnL[i - 1][1] * DnL[i][1]))
        break
print(ans)