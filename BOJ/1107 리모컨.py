import collections


N, M = int(input()), int(input())
ables = set(n for n in range(10))
if M > 0:
    ables -= set(map(int, input().split()))
min_press = abs(N - 100)
q = collections.deque(sorted(list(ables)))
while q:
    tn = q.popleft()
    pressed = len(str(tn)) + abs(N - tn)
    if pressed < min_press:
        min_press = pressed
    for able in ables:
        nxt = tn * 10 + able
        if 0 < nxt <= 1000000:
            q.append(nxt)
print(min_press)
