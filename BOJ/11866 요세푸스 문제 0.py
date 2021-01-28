N, K = map(int, input().split())
nums = [i for i in range(1, N + 1)]
order = [0] * N
f = r = cnt = 0
while cnt < N:
    for _ in range(K - 1):
        nums[f % N] = nums[r % N]
        f = (f + 1) % N
        r = (r + 1) % N
    order[cnt] = nums[r]
    r = (r + 1) % N
    cnt += 1

print('<', end='')
for i in range(N - 1):
    print(order[i], end=', ')
print(f'{order[-1]}>')
