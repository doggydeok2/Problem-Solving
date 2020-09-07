T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    print(f'#{tc} {int(round((sum(arr) - max(arr) - min(arr)) / 8, 0))}')