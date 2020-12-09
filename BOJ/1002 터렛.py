for tc in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dsq = int(x2 - x1) ** 2 + (y2 - y1) ** 2

    if (r2 - r1) ** 2 < dsq < (r2 + r1) ** 2: print(2)
    elif (r1 + r2) ** 2 == dsq or ((r2 - r1) ** 2 == dsq and dsq != 0): print(1)
    elif dsq < (r2 - r1) ** 2 or dsq > (r1 + r2) ** 2: print(0)
    elif not dsq: print(-1)