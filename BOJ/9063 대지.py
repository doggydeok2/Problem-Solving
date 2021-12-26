N = int(input())
min_x = min_y = 10001
max_x = max_y = -10001
for _ in range(N):
    w, h = map(int, input().split())
    min_x = w if min_x > w else min_x
    max_x = w if max_x < w else max_x
    min_y = h if min_y > h else min_y
    max_y = h if max_y < h else max_y

print((max_x - min_x) * (max_y - min_y))
