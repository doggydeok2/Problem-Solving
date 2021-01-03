N, pn = int(input()), 2

while N > 1:
    if N % pn:
        pn += 1
    else:
        N //= pn
        print(pn)