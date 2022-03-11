import itertools


N = int(input())
snowballs = sorted(list(map(int, input().split())))
min_gap = snowballs[N - 1] * 4
for fix1, fix2 in itertools.combinations(range(N - 2), 2):
    l, r = fix2 + 1, fix2 + 2
    while r < N:
        t_gap = snowballs[r] + snowballs[fix1] - snowballs[l] - snowballs[fix2]
        min_gap = min(min_gap, abs(t_gap))
        if t_gap > 0:
            l += 1
            if l == r:
                r += 1
        else:
            r += 1
print(min_gap)
