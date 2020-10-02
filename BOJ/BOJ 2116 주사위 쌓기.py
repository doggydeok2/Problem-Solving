N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
total, totalMax = 0, 0
partner = [5, 3, 4, 1, 2, 0]

for i in range(1, 7):
    p = i
    for dice in dices:
        for n in range(6):
            if dice[n] == p:
                dice[n] = 0
                temp = dice[partner[n]]
                dice[partner[n]] = 0
                total += max(dice)
                dice[n] = p
                p = temp
                dice[partner[n]] = p
                break

    if total > totalMax: totalMax = total
    total = 0
print(totalMax)
