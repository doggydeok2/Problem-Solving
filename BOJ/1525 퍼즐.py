import collections


def get_minimum_move(puzzle, idx):
    q.append((puzzle, idx, 0))
    while q:
        tp, ti, tcnt = q.popleft()
        if tp == '123456780':
            return tcnt
        ltp = list(tp)
        if ti % 3 != 2:
            check_next(ltp, 1, tp, ti, tcnt)
        if ti % 3 != 0:
            check_next(ltp, -1, tp, ti, tcnt)
        if ti // 3 != 0:
            check_next(ltp, -3, tp, ti, tcnt)
        if ti // 3 != 2:
            check_next(ltp, 3, tp, ti, tcnt)
    return -1


def check_next(_ltp, _nxt, _tp, _ti, _tcnt):
    _ltp[_ti], _ltp[_ti + _nxt] = _ltp[_ti + _nxt], _ltp[_ti]
    np = ''.join(_ltp)
    if np not in visited:
        visited.add(np)
        q.append((np, _ti + _nxt, _tcnt + 1))
    _ltp[_ti], _ltp[_ti + _nxt] = _ltp[_ti + _nxt], _ltp[_ti]


q = collections.deque()
visited = set()
init_puzzle = ''
for _ in range(3):
    init_puzzle += ''.join(list(input().split()))
init_idx = init_puzzle.find('0')
print(get_minimum_move(init_puzzle, init_idx))
