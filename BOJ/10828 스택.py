import sys
input = sys.stdin.readline

N = int(input())
stack = [0] * N
ptr = 0
for i in range(N):
    cmd = input()
    if cmd[:3] == 'pop':
        if ptr:
            print(stack[ptr - 1])
            ptr -= 1
        else:
            print(-1)
    if cmd[:3] == 'top':
        print(stack[ptr - 1] if ptr else -1)
    elif cmd[:4] == 'size':
        print(ptr)
    elif cmd[:4] == 'push':
        stack[ptr] = int(cmd[5:])
        ptr += 1
    elif cmd[:5] == 'empty':
        print(0 if ptr else 1)