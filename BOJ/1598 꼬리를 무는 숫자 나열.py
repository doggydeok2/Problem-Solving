A, B = map(int, input().split())
Ax, Ay, Bx, By = A // 4 - (not (A % 4)), A % 4 or 4, B // 4 - (not B % 4), B % 4 or 4
print(abs(Bx - Ax) + abs(By - Ay))
