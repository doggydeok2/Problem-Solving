N = int(input())
arr = list(map(int, input().split()))
subSum = tempSum = arr[0]

for i in range(1, N):
    tempSum = max(tempSum, 0) + arr[i]
    subSum = max(tempSum, subSum)

print(subSum)