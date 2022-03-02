n = int(input())
l, r = 0, n
while l <= r:
    m = (l + r) // 2
    if m ** 2 == n:
        print(m)
        break
    if m ** 2 < n:
        l = m + 1
    else:
        r = m - 1
