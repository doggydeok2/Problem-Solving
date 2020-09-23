W, H = map(int, input().split())
S = int(input())
shops = []
total = 0

for _ in range(S):
    shops += [list(map(int, input().split()))]
    # if p == 1: shops += [0, d]
    # elif p == 2: shops += [H, d]
    # elif p == 3: shops += [d, 0]
    # elif p == 4: shops += [d, W]

Dc, Dd = map(int, input().split())
if Dc == 1:
    for shop in shops:
        if shop[0] == 1: total += abs(Dd - shop[1])
        elif shop[0] == 2: total += min(H + Dd + shop[1], H + 2 * W - Dd - shop[1])
        elif shop[0] == 3: total += Dd + shop[1]
        elif shop[0] == 4: total += W - shop[1] + Dd
elif Dc == 2:
    for shop in shops:
        if shop[0] == 1: total += min(H + Dd + shop[1], H + 2 * W - Dd - shop[1])
        elif shop[0] == 2: total += abs(Dd - shop[1])
        elif shop[0] == 3: total += Dd + H - shop[1]
        elif shop[0] == 4: total += W - shop[1] + H - Dd
elif Dc == 3:
    for shop in shops:
        if shop[0] == 1: total += Dd + shop[1]
        elif shop[0] == 2: total += H - Dd + shop[1]
        elif shop[0] == 3: total += abs(Dd - shop[1])
        elif shop[0] == 4: total += min(shop[1] + Dd + W, W + 2 * H - Dd - shop[1])
elif Dc == 4:
    for shop in shops:
        if shop[0] == 1: total += W - shop[1] + Dd
        elif shop[0] == 2: total += H - Dd + W - shop[1]
        elif shop[0] == 3: total += min(shop[1] + Dd + W, W + 2 * H - Dd - shop[1])
        elif shop[0] == 4: total += abs(Dd - shop[1])

print(total)