import sys
rl = sys.stdin.readline


def check_good_word(_word):
    stack = []
    for ch in _word:
        if not stack or stack and stack[-1] != ch:
            stack.append(ch)
        else:
            stack.pop()
    if stack:
        return 0
    return 1


N = int(rl())
cnt = 0
for _ in range(N):
    cnt += check_good_word(rl().rstrip())
print(cnt)
