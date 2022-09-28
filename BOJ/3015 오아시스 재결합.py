import sys
rl = sys.stdin.readline


N = int(rl())
heights = []
cnt = 0
for _ in range(N):
    t_height = int(rl())
    same = 1
    while heights and heights[-1][0] <= t_height:
        cnt += heights[-1][1]
        if heights[-1][0] == t_height:
            same += heights[-1][1]
        heights.pop()
    if heights:
        cnt += 1
    heights.append((t_height, same))
print(cnt)
