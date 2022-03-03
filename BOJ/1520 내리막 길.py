import collections
dij = [0, -1, 0, 1, 0]

M, N = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(M)]
DP = [[[0] * 4 for __ in range(N)] for _ in range(M)]
q = collections.deque([(0, 0)])
DP[0][0] = [1, 0, 0, 0]
cnt = 0
while q:
    ty, tx = q.popleft()
    for k in range(4):
        ny, nx = ty + dij[k], tx + dij[k + 1]
        if 0 <= ny < M and 0 <= nx < N:
            if nums[ny][nx] < nums[ty][tx]:
                tyx_sum = sum(DP[ty][tx])
                if DP[ny][nx][k] < tyx_sum:
                    DP[ny][nx][k] = tyx_sum
                    q.append((ny, nx))
print(sum(DP[M - 1][N - 1]))
