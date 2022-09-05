from itertools import combinations


S = input()
print(len(list(set([S[a:b] for a, b in combinations([i for i in range(len(S) + 1)], 2)]))))
