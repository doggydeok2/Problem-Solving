import collections


def do_cmd(_n, _cmd):
    if _cmd == 0:
        return (2 * _n) % 10000
    elif _cmd == 1:
        return 9999 if _n == 0 else _n - 1
    elif _cmd == 2:
        return (_n % 1000) * 10 + (_n // 1000)
    return (_n // 10) + (_n % 10) * 1000


cmd = 'DSLR'
T = int(input())
for _ in range(T):
    S, E = map(int, input().split())
    visit = [0] * 10000
    visit[S] = 1
    q = collections.deque([(S, '')])
    while q:
        n, history = q.popleft()
        if n == E:
            print(history)
            break
        for k in range(4):
            nxt = do_cmd(n, k)
            if not visit[nxt]:
                visit[nxt] = 1
                q.append((nxt, history + cmd[k]))
