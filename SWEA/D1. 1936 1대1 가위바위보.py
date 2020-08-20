A, B = map(int, input().split())
cal = (A - B + 3) % 3

if cal == 1: # A 3 B 2 / A 2 B 1  A 1 B 3
    print('A')
else:
    print('B')