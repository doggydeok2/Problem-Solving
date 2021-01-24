n, m = map(int, input().split())
cntTwo = cntFive = 0

for i in range(1, 15):
    cntFive += n // (5 ** i)
    cntFive -= m // (5 ** i)
    cntFive -= (n - m) // (5 ** i)

for i in range(1, 31):
    cntTwo += n // (2 ** i)
    cntTwo -= m // (2 ** i)
    cntTwo -= (n - m) // (2 ** i)

print(min(cntTwo, cntFive))
