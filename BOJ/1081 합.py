def cnt_num(_idx, _n):
    for _i in range(1, 15):
        _nth = 10 ** (_i - 1)
        _over, _under = divmod(_n, _nth)
        _over, _tg = divmod(_over, 10)

        for _x in range(10):
            cnt_nums[_idx][_x] += (_over + (_x < _tg)) * _nth + (_under + 1 if _x == _tg else 0)
            # is equals:
            # if _x < _tg:
            #     cnt_nums[_idx][_x] += (_over + 1) * _nth
            # elif _x == _tg:
            #     cnt_nums[_idx][_x] += _over * _nth + _under + 1
            # else:
            #     cnt_nums[_idx][_x] += _over * _nth
        if _over == 0:
            break


L, U = map(int, input().split())
cnt_nums = [[0] * 10 for _ in range(2)]
cnt_num(0, L - 1)
cnt_num(1, U)
print(sum([i * (cnt_nums[1][i] - cnt_nums[0][i]) for i in range(10)]))
