a, b, c = [int(input()) for _ in range(3)]
if a + b + c != 180:
    print('Error')
elif a == b == c:
    print('Equilateral')
elif a == b or b == c or c == a:
    print('Isosceles')
else:
    print('Scalene')