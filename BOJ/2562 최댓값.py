maxN = i = 0
for t in range(1, 10):
    N = int(input())
    if maxN < N:
        maxN = N
        i = t
print(maxN)
print(i)