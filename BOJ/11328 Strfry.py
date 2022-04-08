def check(_a, _b):
    if len(_a) != len(_b):
        return False
    for i in range(len(_a)):
        if _a[i] != _b[i]:
            return False
    return True


for _ in range(int(input())):
    a, b = input().split()
    a, b = sorted(list(a)), sorted(list(b))
    print('Possible' if check(a, b) else 'Impossible')
