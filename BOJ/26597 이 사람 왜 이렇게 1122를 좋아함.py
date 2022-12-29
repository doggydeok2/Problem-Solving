import sys
rl = sys.stdin.readline


def check():
    up, down = -int(1e18) - 1, int(1e18) + 1
    found = 0
    for i in range(1, int(rl()) + 1):
        n, d = rl().split()
        n = int(n)
        if d == '^':
            up = max(up, n)
        else:
            down = min(down, n)
        if down - up < 2:
            return f'Paradox!\n{i}'
        elif down - up == 2 and found == 0:
            found = i
    return f'I got it!\n{found}' if found else 'Hmm...'


print(check())
