def ap(n):
    int_n = int(n)
    if int_n < 100: return int_n

    cnt = 99
    for i in range(111, int_n + 1):
        flag = 1
        gap = i % 10 - i % 100 // 10
        l = len(str(i))
        for x in range(2, l):
            if i % 10 ** x // 10 ** (x - 1) - i % 10 ** (x + 1) // 10 ** x != gap:
                flag = 0
                break
        if flag: cnt += 1
    return cnt


N = input()
print(ap(N))