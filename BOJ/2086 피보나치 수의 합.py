def get_fibo(_n):
    if _n == 1:
        return 1, 1, 1, 0
    _a, _b, _c, _d = get_fibo(_n // 2)
    _a, _b, _c, _d = (_a ** 2 + _b * _c) % mod, (_a * _b + _b * _d) % mod,\
                     (_a * _c + _c * _d) % mod, (_b * _c + _d ** 2) % mod
    if _n % 2 == 1:
        _a, _b, _c, _d = (_a + _b) % mod, _a, (_c + _d) % mod, _c
    return _a, _b, _c, _d


mod = 1000000000
a, b = map(int, input().split())
print((get_fibo(b + 1)[0] - get_fibo(a)[0] + mod) % mod)
