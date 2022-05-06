N = int(input())
ramens = list(map(int, input().split())) + [0, 0]
ans = 0
for i in range(N):
    if ramens[i + 1] > ramens[i + 2]:
        gap = min(ramens[i + 1] - ramens[i + 2], ramens[i])
        ramens[i + 1] -= gap
        ramens[i] -= gap
        ans += gap * 5
    m3 = min(ramens[i], ramens[i + 1], ramens[i + 2])
    ans += m3 * 7
    ramens[i] -= m3
    ramens[i + 1] -= m3
    ramens[i + 2] -= m3
    m2 = min(ramens[i], ramens[i + 1])
    ans += m2 * 5
    ramens[i + 1] -= m2
    ramens[i] -= m2
    ans += ramens[i] * 3
print(ans)
