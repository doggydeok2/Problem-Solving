N = int(input())
nums = list(map(int, input().split()))
ans = acc = 0
for num in nums:
    ans = (ans + acc * num) % 1000000007
    acc = (acc + num) % 1000000007
print(ans)
