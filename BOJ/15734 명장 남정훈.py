L, R, A = map(int, input().split())
if R > L:
    L, A = L + min(R - L, A), A - min(R - L, A)
else:
    R, A = R + min(L - R, A), A - min(L - R, A)
print(2 * (min(L, R) + A // 2))
