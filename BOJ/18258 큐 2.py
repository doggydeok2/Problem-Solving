import sys
inSys = sys.stdin.readline

N = int(inSys())
q = [0] * N
f = r = 0
for _ in range(N):
    cmd = inSys()
    if cmd[:3] == 'pop':
        if f != r:
            print(q[f])
            f += 1
        else:
            print(-1)
    elif cmd[:4] == 'push':
        q[r] = cmd[5:-1]
        r += 1
    elif cmd[:4] == 'size':
        print(r - f)
    elif cmd[:4] == 'back':
        print(q[r - 1] if f != r else -1)
    elif cmd[:5] == 'front':
        print(q[f] if f != r else -1)
    elif cmd[:5] == 'empty':
        print(1 if f == r else 0)
