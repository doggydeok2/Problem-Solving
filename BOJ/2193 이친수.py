N = int(input())
DP_arr = [0] * (N + 1)
DP_arr[1] = 1

for i in range(2, N + 1):
    DP_arr[i] = DP_arr[i - 1] + DP_arr[i - 2]

print(DP_arr[N])
