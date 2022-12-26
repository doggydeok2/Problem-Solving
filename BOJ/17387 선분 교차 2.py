def ccw(_x1, _y1, _x2, _y2, _x3, _y3):
    d = _x1 * _y2 + _x2 * _y3 + _x3 * _y1 - _x1 * _y3 - _x3 * _y2 - _x2 * _y1
    return 1 if d > 0 else -1 if d < 0 else 0


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
if x1 > x2 or x1 == x2 and y1 > y2:
    x1, y1, x2, y2 = x2, y2, x1, y1
if x3 > x4 or x3 == x4 and y3 > y4:
    x3, y3, x4, y4 = x4, y4, x3, y3

c123, c124 = ccw(x1, y1, x2, y2, x3, y3), ccw(x1, y1, x2, y2, x4, y4)
c341, c342 = ccw(x3, y3, x4, y4, x1, y1), ccw(x3, y3, x4, y4, x2, y2)

if c123 * c124 == 0 and c341 * c342 == 0:
    if x1 == x2 == x3 == x4:
        print(1 if y3 <= y2 and y1 <= y4 else 0)
    else:
        print(1 if x3 <= x2 and x1 <= x4 else 0)
else:
    print(1 if c123 * c124 <= 0 and c341 * c342 <= 0 else 0)
