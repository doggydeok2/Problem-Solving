import sys
rl = sys.stdin.readline
sys.setrecursionlimit(200002)


def dfs(_s, _n):
    nxt = wants[_n]
    if visited[nxt] == 0:
        visited[nxt] = _s
        visited[_n] = dfs(_s, nxt)
        return visited[_n] if _n != visited[_n] else -1
    elif visited[nxt] == _s:
        visited[_n] = nxt
        return nxt if _n != nxt else -1
    else:
        visited[_n] = -1
        return -1


visited = []
for _ in range(int(rl())):
    n = int(rl())
    wants = [0] + list(map(int, rl().split()))
    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        if visited[i] == 0:
            visited[i] = i
            dfs(i, i)
    print(visited.count(-1))
