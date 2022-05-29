import itertools
import collections


def solve():
    # comb = itertools.combinations([i for i in range(M)], 2)
    visited = [0] * 1000001
    q = collections.deque([(N, 1)])
    max_n = -1
    while q:
        t_num, t_cnt = q.popleft()
        if t_cnt > K:
            max_n = max(max_n, int(t_num))
            continue
        t_num = list(t_num)
        for i, j in itertools.combinations([i for i in range(M)], 2):
            n_num = t_num[:]
            n_num[i], n_num[j] = n_num[j], n_num[i]
            n_num_int = int(''.join(n_num))
            if visited[n_num_int] == t_cnt:
                continue
            if n_num_int // (10 ** (M - 1)) == 0:
                continue
            visited[n_num_int] = t_cnt
            q.append((str(n_num_int), t_cnt + 1))

    return max_n


N, K = input().split()
K = int(K)
M = len(N)
print(solve())