N, S = map(int, input().split())
nums = list(map(int, input().split()))
part_sum = [0]

for num in nums:
    for i in range(len(part_sum)):
        part_sum.append(num + part_sum[i])

print(part_sum.count(S) - (1 if S == 0 else 0))
