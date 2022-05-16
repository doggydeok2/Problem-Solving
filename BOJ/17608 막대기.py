N = int(input())
sticks = [int(input()) for _ in range(N)]
cnt = max_h = 0
for i in range(N - 1, -1, -1):
    if sticks[i] > max_h:
        cnt += 1
        max_h = sticks[i]
print(cnt)
