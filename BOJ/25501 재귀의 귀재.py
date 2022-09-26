def recursion(_str, _i):
    if len(_str) // 2 < _i:
        return True
    global cnt
    cnt += 1
    return _str[_i] == _str[-(_i + 1)] and recursion(_str, _i + 1)


for _ in range(int(input())):
    string = input()
    cnt = 0
    print(1 if recursion(string, 0) else 0, cnt)
