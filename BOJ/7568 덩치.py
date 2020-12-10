N = int(input())
hws = [list(map(int, input().split())) for _ in range(N)]
rating = [1] * N

for i in range(N):
    H, W = hws[i]
    for h, w in hws:
        if H < h and W < w:
            rating[i] += 1

for i in range(N):
    print(rating[i], end=' ')
print()
