J, G = list(map(int, input().split())), list(map(int, input().split()))
s, win_once, turn = 0, False, False
for i in range(9):
    s += J[i]
    win_once = win_once or s > 0
    s -= G[i]
    turn = turn or s < 0
print('Yes' if win_once and turn else 'No')
