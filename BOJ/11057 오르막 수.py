N = int(input())
DP_arr = [1] * 10
for i in range(1, N + 1):
    for j in range(10):
        DP_arr[j] = sum(DP_arr[j:]) % 10007
print(DP_arr[0])
