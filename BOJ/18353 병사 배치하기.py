N = int(input())
powers = list(map(int, input().split()))
check_arr = [1] * N

for idx, power in enumerate(powers):
    for i in range(idx - 1, -1, -1):
        if power < powers[i]:
            check_arr[idx] = max(check_arr[i] + 1, check_arr[idx])

print(N - max(check_arr))
