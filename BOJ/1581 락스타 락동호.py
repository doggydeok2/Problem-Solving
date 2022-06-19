FF, FS, SF, SS = map(int, input().split())
ans = 0
if FF == FS == 0:
    ans = SS + (not not SF)
else:
    ans += FF
    if FS:
        ans += 1 + SS + 2 * min(SF, FS - 1) + (SF > FS - 1)
print(ans)
