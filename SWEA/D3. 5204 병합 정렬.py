def dnc(a):
    global cnt
    a_len = len(a)
    if a_len < 2: return a
 
    m = a_len // 2
    al, ar = dnc(a[0:m]), dnc(a[m:a_len])
    al_len, ar_len = len(al), len(ar)
    ais = [0] * a_len
    ptr1, ptr2, ptr = 0, 0, 0
 
    while ptr1 < al_len and ptr2 < ar_len:
        if al[ptr1] > ar[ptr2]:
            ais[ptr] = ar[ptr2]
            ptr2 += 1
        else:
            ais[ptr] = al[ptr1]
            ptr1 += 1
        ptr += 1
 
    if ptr1 < al_len: cnt += 1
    while ptr1 < al_len:
        ais[ptr] = al[ptr1]
        ptr += 1
        ptr1 += 1
    while ptr2 < ar_len:
        ais[ptr] = ar[ptr2]
        ptr += 1
        ptr2 += 1
 
    return ais
 
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    cnt = 0
 
    so = dnc(ai)
    print(f'#{tc} {so[N // 2]} {cnt}')