try:
    while True:
        x = input()
        ans = [0] * 4
        for ch in x:
            if ch.islower():
                ans[0] += 1
            elif ch.isupper():
                ans[1] += 1
            elif ch.isspace():
                ans[3] += 1
            else:
                ans[2] += 1
        print(*ans)
except:
    pass
