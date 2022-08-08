try:
    while True:
        n = int(input())
        ones = cnt = 1
        while ones % n:
            cnt += 1
            ones = (ones * 10 + 1) % n
        print(cnt)
except:
    pass
