cntFive = 0
for i in range(5, int(input()) + 1, 5):
    while not i % 5:
        cntFive += 1
        i //= 5
print(cntFive)
