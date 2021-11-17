n, x = int(input()), list(map(int, input().split()))

acc_sum, ans = [x[0]], 0
for i in range(1, n - 1):
  acc_sum.append(acc_sum[-1] + x[i])
for i in range(1, n):
  ans += x[-i] * acc_sum[-i]
print(ans)
