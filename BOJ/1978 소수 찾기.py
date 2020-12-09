N = int(input())
nums = list(map(int, input().split()))
for num in nums:
    if num == 1: N -= 1
    for i in range(2, num):
        if not num % i:
            N -= 1
            break
print(N)
    