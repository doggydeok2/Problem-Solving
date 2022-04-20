arr = list(map(int, input().split()))
for i in range(5):
    for j in range(1, 5 - i):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            print(*arr)
