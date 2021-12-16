def num_to_str(n):
    return str(n) if n >= 10 else '0' + str(n)


N, K = map(int, input().split())
K = str(K)
cnt = 0

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if K in num_to_str(h) + num_to_str(m) + num_to_str(s):
                cnt += 1
print(cnt)
