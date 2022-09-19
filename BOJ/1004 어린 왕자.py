for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for n in range(int(input())):
        cx, cy, r = map(int, input().split())
        ans += ((cx - x1) ** 2 + (cy - y1) ** 2 < r ** 2) ^ ((cx - x2) ** 2 + (cy - y2) ** 2 < r ** 2)
    print(ans)
