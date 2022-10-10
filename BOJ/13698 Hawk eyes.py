def change(_i, _j):
    cups[_i], cups[_j] = cups[_j], cups[_i]


cups = [1, 0, 0, 2]
for ch in input():
    if ch == 'A': change(0, 1)
    elif ch == 'B': change(0, 2)
    elif ch == 'C': change(0, 3)
    elif ch == 'D': change(1, 2)
    elif ch == 'E': change(1, 3)
    else: change(2, 3)
print(f'{1 + cups.index(1)}\n{1 + cups.index(2)}')
