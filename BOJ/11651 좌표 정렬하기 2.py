import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, input().split()))
for ptr in sorted(arr, key=lambda x: (x[1], x[0])):
    print(ptr[0], ptr[1])