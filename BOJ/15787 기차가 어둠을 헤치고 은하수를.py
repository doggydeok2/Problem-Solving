import sys
rl = sys.stdin.readline


N, M = map(int, rl().split())
trains = [0] * N
full = 2 ** 20 - 1
for _ in range(M):
    cmd = rl().rstrip()
    if cmd[0] == '1':
        c, i, x = map(int, cmd.split())
        trains[i - 1] |= 1 << (x - 1)
    elif cmd[0] == '2':
        c, i, x = map(int, cmd.split())
        trains[i - 1] &= full - (1 << (x - 1))
    elif cmd[0] == '3':
        c, i = map(int, cmd.split())
        trains[i - 1] <<= 1
        trains[i - 1] &= full
    else:
        c, i = map(int, cmd.split())
        trains[i - 1] >>= 1
print(len(set(trains)))
