def dp(a, b):
    checked = [(a, 1)]
    ptr = 0

    while ptr < len(checked):
        val, cnt = checked[ptr]
        if val * 2 == B or val * 10 + 1 == B:
            return cnt + 1
        if val * 10 + 1 < B:
            checked.append((val * 10 + 1, cnt + 1))
        if val * 2 < B:
            checked.append((val * 2, cnt + 1))
        ptr += 1
    return -1


A, B = map(int, input().split())
print(dp(A, B))
