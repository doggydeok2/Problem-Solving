def left_check(idx):
    max_cnt = 1
    for x in range(idx - 1, -1, -1):
        if A[x] < A[idx]:
            max_cnt = max(left_cnt[x] + 1, max_cnt)
    return max_cnt


def right_check(idx):
    max_cnt = 1
    for x in range(idx + 1, N):
        if A[idx] > A[x]:
            max_cnt = max(right_cnt[x] + 1, max_cnt)
    return max_cnt


N, A = int(input()), list(map(int, input().split()))
left_cnt, right_cnt = [1] * N, [1] * N

for i in range(1, N):
    left_cnt[i] = left_check(i)
    right_cnt[N - 1 - i] = right_check(N - 1 - i)

print(max([left_cnt[x] + right_cnt[x] for x in range(N)]) - 1)
