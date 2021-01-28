import sys
input = sys.stdin.readline

N = int(input())
q = [0] * N
size = f = r = 0
for _ in range(N):
    cmd = input()
    if cmd[:4] == 'size':
        print(size)
    elif cmd[:4] == 'back':
        print(q[r] if f != r else -1)
    elif cmd[:5] == 'front':
        print(q[(f - 1) % N] if f != r else -1)
    elif cmd[:5] == 'empty':
        print(1 if f == r else 0)
    elif cmd[:5] == 'pop_f':
        if f == r:
            print(-1)
        else:
            f = (f - 1) % N
            print(q[f])
            size -= 1
    elif cmd[:5] == 'pop_b':
        if f == r:
            print(-1)
        else:
            print(q[r])
            r = (r + 1) % N
            size -= 1
    elif cmd[:6] == 'push_b':
        r = (r - 1) % N
        q[r] = cmd[10:-1]
        size += 1
    elif cmd[:6] == 'push_f':
        q[f] = cmd[11:-1]
        f = (f + 1) % N
        size += 1
