for tc in range(int(input())):
    H, W, N = map(int, input().split())
    h = N % H or H
    w = N // H + bool(N % H)
    w = str(w).zfill(2) if w < 10 else str(w)
    print('%d%s' % (h, w))