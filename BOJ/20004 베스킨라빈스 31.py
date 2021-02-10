A = int(input())
for i in range(2, A + 2):
    s = 30
    while s - i > 0:
        s -= i
    if s > i - 1:
        print(i - 1)
