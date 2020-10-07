N = int(input())
P = list(map(int, input().split()))
cnt, minTotal = N, 0
P.sort()
for pi in P:
    minTotal += pi * cnt
    cnt -= 1
print(minTotal)