T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    v, d = 0, 0
    for _ in range(N):
        cmd = input()
        if cmd[0] == '1':
            v += int(cmd[2])
        elif cmd[0] == '2':
            v -= int(cmd[2])
            if v < 0: v = 0
        d += v
    print(f'#{tc} {d}')