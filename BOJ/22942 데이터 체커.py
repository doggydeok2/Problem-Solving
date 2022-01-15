import sys
rl = sys.stdin.readline


def check_data():
    N = int(rl())
    circles = [() for _ in range(N)]

    for i in range(N):
        x, r = map(int, rl().split())
        circles[i] = (x - r, x + r)

    circles.sort()
    stack = []
    for l, r in circles:
        while stack and stack[-1][1] < l:
            stack.pop()
        if not stack or stack[-1][0] < l and r < stack[-1][1]:
            stack.append((l, r))
        else:
            return False
    return True


print('YES' if check_data() else 'NO')
