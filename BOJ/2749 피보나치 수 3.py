def nth_power(_n):
    if _n == 1:
        return 1, 1, 1, 0
    _a, _b, _c, _d = nth_power(_n // 2)
    _a, _b, _c, _d = (_a ** 2 + _b * _c) % 1000000, \
                     (_a * _b + _b * _d) % 1000000, \
                     (_c * _a + _d * _c) % 1000000, \
                     (_b * _c + _d ** 2) % 1000000
    if _n % 2:
        _a, _b, _c, _d = (_a + _b) % 1000000, _a, (_c + _d) % 1000000, _c
    return _a, _b, _c, _d


n = int(input())
print(1 if n == 1 else nth_power(n - 1)[0])
