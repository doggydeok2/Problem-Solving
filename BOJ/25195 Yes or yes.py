import sys
sys.setrecursionlimit(100002)
rl = sys.stdin.readline


def dfs(_n):
    if fan_list[_n]:
        return False
    if not adl[_n]:
        return True
    for nxt in adl[_n]:
        if dfs(nxt):
            return True


N, M = map(int, input().split())
adl = [[] for _ in range(N + 1)]
fan_list = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, rl().split())
    adl[s].append(e)

int(rl())
fans = list(map(int, rl().split()))
for fan in fans:
    fan_list[fan] = 1
print('yes' if dfs(1) else 'Yes')