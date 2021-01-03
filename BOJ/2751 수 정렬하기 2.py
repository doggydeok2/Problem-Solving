def dnc(l, r):
    if r - l == 1: return

    m = (l + r) // 2
    al_l, ar_l = m - l, r - m
    if al_l > 1: dnc(l, m)
    if ar_l > 1: dnc(m, r)
    al, ar = arr[l:m], arr[m:r]

    x = l
    lp = rp = 0
    while lp < al_l and rp < ar_l:
        if al[lp] > ar[rp]:
            arr[x] = ar[rp]
            rp += 1
        else:
            arr[x] = al[lp]
            lp += 1
        x += 1
    while lp < al_l:
        arr[x] = al[lp]
        lp += 1
        x += 1
    while rp < ar_l:
        arr[x] = ar[rp]
        rp += 1
        x += 1


N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
dnc(0, N)
for num in arr: print(num)