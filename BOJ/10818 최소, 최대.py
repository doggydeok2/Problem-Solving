N = int(input())
arr = list(map(int, input().split()))
minN, maxN = 1000000, -1000000
for n in arr:
    if minN > n: minN = n
    if maxN < n: maxN = n

print(minN, maxN)