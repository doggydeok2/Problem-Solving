N, M = map(int, input().split())
nums = list(map(int, input().split()))
acc = [0] * N
cnt_arr = [0] * (M + 1)
ans = 0
for i in range(N):
    acc[i] = (acc[i - 1] + nums[i]) % M
for i in range(N):
    cnt_arr[acc[i]] += 1
    ans += cnt_arr[acc[i]] - (acc[i] != 0)
print(ans)
