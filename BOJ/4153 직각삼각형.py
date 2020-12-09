
while True:
    X, Y, Z = map(int, input().split())
    if not X and not Y and not Z: break
    print('right') if X ** 2 + Y ** 2 == Z ** 2 or Y ** 2 + Z ** 2 == X ** 2 or Z ** 2 + X ** 2 == Y **2 else print('wrong')