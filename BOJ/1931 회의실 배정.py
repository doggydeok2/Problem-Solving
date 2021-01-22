N = int(input())
I = [[0, 0] for _ in range(N)]
for i in range(N):
    I[i] = list(map(int, input().split()))
I.sort()
v = [0] * N
able = cnt = 0
for i in range(N):
    s, e = I[i][0], I[i][1]
    if s >= able:
        cnt += 1
        v[i] = cnt
        able = e
    elif s < able and e < able:
        v[i] = cnt
        able = e
    else:
        v[i] = cnt

print(cnt)
