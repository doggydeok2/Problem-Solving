N = int(input())
nums = list(map(int, input().split()))
asc, ascMax, desc, descMax = 1, 0, 1, 0

for i in range(1, N):
    if nums[i] == nums[i - 1]:
        asc += 1
        desc += 1
    elif nums[i - 1] > nums[i]:
        desc += 1
        if ascMax < asc: ascMax = asc
        asc = 1
    elif nums[i - 1] < nums[i]:
        asc += 1
        if descMax < desc: descMax = desc
        desc = 1

if ascMax < asc: ascMax = asc
if descMax < desc: descMax = desc

print(max(ascMax, descMax))
