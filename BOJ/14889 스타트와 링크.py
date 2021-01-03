def calculating():
    global minGap
    gap = 0
    for idx in one:
        for idx2 in one:
            gap += synergies[idx][idx2]
    for idx in two:
        for idx2 in two:
            gap -= synergies[idx][idx2]
    minGap = min(abs(gap), minGap)


def dividing(n, l, r):
    if l == N // 2:
        for i in range(N // 2 - r):
            two[r + i] = n + i
        calculating()
    elif r == N // 2:
        for i in range(N // 2 - l):
            one[l + i] = n + i
        calculating()
    else:
        one[l] = n
        dividing(n + 1, l + 1, r)
        one[l] = 0
        two[r] = n
        dividing(n + 1, l, r + 1)
        two[r] = 0


N = int(input())
synergies = [list(map(int, input().split())) for _ in range(N)]
one, two = [0] * (N // 2), [0] * (N // 2)
minGap = 40000

dividing(1, 1, 0)
print(minGap)
