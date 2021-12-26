import sys
rl = sys.stdin.readline
wr = sys.stdout.write

T = int(rl())
for tc in range(1, T + 1):
    wr(f'PROGRAM #{tc}:\n')
    cmd, out, err = '', [], False
    com, ptr = [0] * 256, 1
    brackets_stack, brackets_dict = [], {}

    while True:
        cmd_row = rl()
        if cmd_row == 'end\n':
            break
        cmd += cmd_row.split('%')[0]

    for i in range(len(cmd)):
        if cmd[i] == '[':
            brackets_stack.append(i)
        elif cmd[i] == ']':
            if not len(brackets_stack):
                err = True
                break
            left_idx = brackets_stack.pop()
            brackets_dict[left_idx] = i
            brackets_dict[i] = left_idx

    if len(brackets_stack) or err:
        wr('COMPILE ERROR\n')
    else:
        i = 0
        while i < len(cmd):
            ch = cmd[i]
            if ch == '>':
                ptr = 0 if ptr == 255 else ptr + 1
            elif ch == '<':
                ptr = 255 if ptr == 0 else ptr - 1
            elif ch == '+':
                com[ptr] = 0 if com[ptr] == 32767 else com[ptr] + 1
            elif ch == '-':
                com[ptr] = 32767 if com[ptr] == 0 else com[ptr] - 1
            elif ch == '.':
                out.append(chr(com[ptr]))
            elif ch == '[' and com[ptr] == 0:
                i = brackets_dict[i] - 1
            elif ch == ']' and not com[ptr] == 0:
                i = brackets_dict[i] - 1
            # else pass
            i += 1
        wr(''.join(out) + '\n')
