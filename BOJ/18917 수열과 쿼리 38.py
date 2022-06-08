import sys
rl = sys.stdin.readline


M = int(rl())
ans_sum = ans_xor = 0
for _ in range(M):
    cmd = rl().rstrip()
    if cmd == '3':
        print(ans_sum)
    elif cmd == '4':
        print(ans_xor)
    else:
        x, n = map(int, cmd.split())
        ans_xor ^= n
        ans_sum += n if x == 1 else -n
