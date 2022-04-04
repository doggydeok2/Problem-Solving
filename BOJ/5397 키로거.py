import sys
rl = sys.stdin.readline


for tc in range(int(rl())):
    out, tmp = [], []
    cmds = rl().rstrip()
    for cmd in cmds:
        if cmd == '<':
            if out:
                tmp.append(out.pop())
        elif cmd == '>':
            if tmp:
                out.append(tmp.pop())
        elif cmd == '-':
            if out:
                out.pop()
        else:
            out.append(cmd)
    out.extend(reversed(tmp))
    print(''.join(out))
