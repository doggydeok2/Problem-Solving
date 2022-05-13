def get_final_length(_sl, _n):
    for i in range(_n):
        if _sl + i < heights[i]:
            return _sl + i
    return _sl + _n


N, L = map(int, input().split())
heights = sorted(list(map(int, input().split())))
print(get_final_length(L, N))
