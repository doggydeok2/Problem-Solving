S = int(input())
n, nxt = 0, 1
while n <= S:
    n += nxt
    nxt += 1
print(nxt - 2)
