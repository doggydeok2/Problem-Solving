def bingo_col(x):
    for i in range(5):
        if table[x][i]: return 0
    return 1


def bingo_row(x):
    for i in range(5):
        if table[i][x]: return 0
    return 1


def bingo_diagonal():
    for i in range(5):
        if table[i][i]: return 0
    return 1


def bingo_diagonal2():
    for i in range(5):
        if table[4 - i][i]: return 0
    return 1


table = [list(map(int, input().split())) for _ in range(5)]
cnt, flag = 0, 0

for _ in range(5):
    calls = list(map(int, input().split()))
    for call in calls:
        cnt += 1
        for j in range(5):
            for i in range(5):
                if table[j][i] == call:
                    table[j][i] = 0

        for i in range(5):
            flag += bingo_col(i)
            flag += bingo_row(i)
        flag += bingo_diagonal()
        flag += bingo_diagonal2()
        if flag >= 3: break
        else: flag = 0
    if flag >= 3: break

print(cnt)