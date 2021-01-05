N = int(input())
arr = list(map(int, input().split()))
nthArr = [0] * 1001
for num in arr:
    nthArr[num] = max(nthArr[:num]) + 1
print(max(nthArr))