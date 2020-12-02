for tc in range(1, int(input()) + 1):
    data = list(map(int, input().split()))
    N = data[0]
    data = data[1:]
    avg = sum(data) / N

    n = 0
    for sc in data:
        if sc > avg:
            n += 1
    ans = n / N * 100
    print('%0.3f%%' % ans)

