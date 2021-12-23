import sys
rl = sys.stdin.readline
wr = sys.stdout.write

M = int(rl().rstrip())
S = set()
for _ in range(M):
    cmd = rl().rstrip()
    if cmd == "all":
        S.update(range(1, 21))
    elif cmd == "empty":
        S.clear()
    else:
        cmd, x = cmd.split()
        x = int(x)
        if cmd == "add":
            S.add(x)
        elif cmd == "remove":
            S.discard(x)
        elif cmd == "check":
            wr('1\n' if x in S else '0\n')
        else:
            if x in S:
                S.discard(x)
            else:
                S.add(x)
