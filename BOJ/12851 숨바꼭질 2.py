import collections


def visit_valid(_idx, _time):
    return visit_times[_idx] == -1 or visit_times[_idx] == _time + 1


def visit_check(_idx, _time):
    position[_idx] += 1
    visit_times[_idx] = _time + 1
    q.append((_idx, _time + 1))


N, K = map(int, input().split())
position = [0] * 100001
visit_times = [-1] * 100001
visit_times[N], position[N] = 0, 1

q = collections.deque([(N, 0)])
while q:
    me, time = q.popleft()
    if visit_times[K] != -1 and visit_times[K] < time:
        break
    if me + 1 < 100001 and visit_valid(me + 1, time):
        visit_check(me + 1, time)
    if me - 1 >= 0 and visit_valid(me - 1, time):
        visit_check(me - 1, time)
    if me * 2 < 100001 and visit_valid(me * 2, time):
        visit_check(me * 2, time)

print(f'{visit_times[K]}\n{position[K]}')
