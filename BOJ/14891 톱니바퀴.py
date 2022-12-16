saw_teeth = [input() for _ in range(4)]
meets = [[6, 2] for _ in range(4)]
for _ in range(int(input())):
    rotate = [0] * 4
    n, d = map(int, input().split())
    rotate[n - 1] = d
    for i in range(n, 4):
        if saw_teeth[i - 1][meets[i - 1][1]] == saw_teeth[i][meets[i][0]]:
            break
        rotate[i] = -rotate[i - 1]
    for i in range(n - 1, 0, -1):
        if saw_teeth[i][meets[i][0]] == saw_teeth[i - 1][meets[i - 1][1]]:
            break
        rotate[i - 1] = -rotate[i]
    for i in range(4):
        if rotate[i]:
            meets[i][0] = (meets[i][0] - rotate[i]) % 8
            meets[i][1] = (meets[i][1] - rotate[i]) % 8
print(sum([(saw_teeth[i][(meets[i][0] + 2) % 8] == '1') * (1 << i) for i in range(4)]))
