import bisect
import sys
rl = sys.stdin.readline


N = int(rl())
lines = sorted([list(map(int, rl().split())) for _ in range(N)])
line_ends = [lines[i][1] for i in range(N)]

LIS_idx = [-1] * N
LIS = []
for i, e in enumerate(line_ends):
    idx = bisect.bisect(LIS, e)
    if idx == len(LIS):
        LIS.append(e)
    else:
        LIS[idx] = e
    LIS_idx[i] = idx

ans = []
l = len(LIS) - 1
for i in range(N - 1, -1, -1):
    if LIS_idx[i] == l:
        l -= 1
        continue
    ans.append(lines[i][0])

l = len(ans)
print(l)
for i in range(l - 1, -1, -1):
    print(ans[i])
