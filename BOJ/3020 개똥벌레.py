import sys
rl = sys.stdin.readline


N, H = map(int, rl().split())
obstacles = [int(rl()) for _ in range(N)]
tops, bottoms = [0] * H, [0] * H
for i, h in enumerate(obstacles):
    if i % 2:
        tops[h] += 1
    else:
        bottoms[h] += 1
top_acc = [0] * H
bot_acc = [0] * H
for i in range(1, H):
    top_acc[i] = top_acc[i - 1] + tops[i]
    bot_acc[i] = bot_acc[i - 1] + bottoms[i]
destroys = [N - bot_acc[H - 1 - i] - top_acc[i] for i in range(H)]
print(min(destroys), destroys.count(min(destroys)))