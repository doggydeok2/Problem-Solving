def ans(_m):
    if len(_m) == M:
        print(*_m)
    else:
        for num in nums:
            ans(_m + [num])


N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans([])
