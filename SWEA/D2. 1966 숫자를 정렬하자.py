T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    for j in range(N):
        for i in range(N - 1):
            if arr[i] > arr[i + 1]: arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(f'#{tc}', end = ' ')
    for num in arr:
        print(num, end = ' ')
    print()