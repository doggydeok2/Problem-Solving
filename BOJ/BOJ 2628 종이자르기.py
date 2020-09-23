W, H = map(int, input().split())
C = int(input())
rArr, cArr = [0] * (C + 1) + [H], [0] * (C + 1) + [W]
r, c, SMax = 1, 1, 0
for _ in range(C):
    co, n = map(int, input().split())
    if co:
        cArr[c] = n
        c += 1
    else:
        rArr[r] = n
        r += 1

cArr.sort()
rArr.sort()

for i in range(C - c, C + 1):
    for j in range(C - r, C + 1):
        S = (rArr[j + 1] - rArr[j]) * (cArr[i + 1] - cArr[i])
        if SMax < S: SMax = S

print(SMax)