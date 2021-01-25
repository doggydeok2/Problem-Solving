n = int(input())
goal = [int(input()) for _ in range(n)]
stack = [0] * n
ptr = ptrG = 0
cmd = []

for i in range(1, n + 1):
    stack[ptr] = i
    cmd.append('+')
    while 0 <= ptr < n and 0 <= ptrG < n and stack[ptr] == goal[ptrG]:
        cmd.append('-')
        ptr -= 1
        ptrG += 1
    ptr += 1

if ptrG == n:
    for op in cmd:
        print(op)
else:
    print('NO')
