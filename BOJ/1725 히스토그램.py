import sys
rl = sys.stdin.readline


N = int(rl())
stack = []
max_size = 0
for i in range(N):
    h, fi = int(rl()), i
    while stack and stack[-1][0] >= h:
        ph, pi = stack.pop()
        max_size = max(max_size, ph * (i - pi))
        fi = pi
    stack.append((h, fi))

while stack:
    th, ti = stack.pop()
    max_size = max(max_size, th * (N - ti))
print(max_size)
