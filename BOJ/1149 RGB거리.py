N = int(input())
arr = [0] * 3

for i in range(N):
    R, G, B = map(int, input().split())
    arr[0], arr[1], arr[2] = min(arr[1] + R, arr[2] + R), min(arr[0] + G, arr[2] + G), min(arr[0] + B, arr[1] + B)
print(min(arr))