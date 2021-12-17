K, N = map(int, input().split())
LANs = [int(input()) for _ in range(K)]
left, mid, right = 1, 0, max(LANs)
max_len = 0

while left <= right:
    mid = (left + right) // 2 or 1
    cnt = 0
    for LAN in LANs:
        cnt += LAN // mid
    if cnt < N:
        right = mid - 1
    else:
        max_len = mid
        left = mid + 1
print(max_len)
