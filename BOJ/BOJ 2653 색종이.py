P = int(input())
paper = [[0] * 100 for _ in range(100)]

for _ in range(P):
    x, y = map(int, input().split())
    for i in range(x - 1, x + 9):
        for j in range(y - 1, y + 9):
            paper[j][i] = 1

cnt = 0
for j in range(100):
    for i in range(100):
       if paper[j][i]: cnt += 1

print(cnt)