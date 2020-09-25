data = [[0] * 100 for _ in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for i in range(x1, x2):
            data[j][i] = 1

cnt = 0
for line in data:
    for n in line:
        if n: cnt += 1

print(cnt)