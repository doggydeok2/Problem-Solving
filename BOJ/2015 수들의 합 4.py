from collections import defaultdict


N, K = map(int, input().split())
nums = list(map(int, input().split()))
acc = [0] * N
for i in range(N):
    acc[i] = acc[i - 1] + nums[i]

acc_dict = defaultdict(int)
ans = 0
for i, t_acc in enumerate(acc):
    ans += acc_dict[t_acc - K]
    if t_acc == K:
        ans += 1
    acc_dict[t_acc] += 1
print(ans)
