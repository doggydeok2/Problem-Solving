def more_tries(_x, _y):
    _Z = 100 * _y // _x
    if _Z >= 99:
        return -1
    _l, _r = 0, _x * 2
    _ables = _r
    while _l <= _r:
        _mid = (_l + _r) // 2
        if _Z + 1 <= 100 * (_y + _mid) // (_x + _mid):
            _ables = min(_ables, _mid)
            _r = _mid - 1
        else:
            _l = _mid + 1
    return _ables


X, Y = map(int, input().split())
print(more_tries(X, Y))
