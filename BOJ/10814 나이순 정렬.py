import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N

for i in range(N):
    arr[i] = list(input().split())
    arr[i][0] = int(arr[i][0])

for age, name in sorted(arr, key=lambda x: x[0]):
    print(age, name)