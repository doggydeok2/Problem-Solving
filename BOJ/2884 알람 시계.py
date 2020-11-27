H, M = map(int, input().split())
if M >= 45: print(H, M - 45)
elif not H:
    print(23, M + 15)
else:
    print(H - 1, M + 15)