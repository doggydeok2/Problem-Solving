for tc in range(int(input())):
    x, y = map(int, input().split())
    d = y - x
    total = cnt = 0
    for i in range(1, 2**31):
        total += i
        cnt += 1
        if total >= d: break
        total += i
        cnt += 1
        if total >= d: break
    print(cnt)
