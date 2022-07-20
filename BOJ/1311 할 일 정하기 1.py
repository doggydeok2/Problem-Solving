from itertools import combinations


N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
DP = [262143] * (2 ** N)
DP[0] = 0
for i in range(N):
    for j in combinations([2 ** x for x in range(N)], i):
        sum_j = sum(j)
        for t in range(N):
            is_accepted = sum_j & 2 ** t
            if is_accepted:
                continue
            accepted = sum_j | 2 ** t
            DP[accepted] = min(DP[accepted], DP[sum_j] + costs[i][t])
print(DP[-1])
