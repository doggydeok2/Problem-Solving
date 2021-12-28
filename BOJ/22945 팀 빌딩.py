N = int(input())
powers = list(map(int, input().split()))
left, right = 0, N - 1
max_power = 0
while left < right:
    lp, rp = powers[left], powers[right]
    temp_power = (right - left - 1) * min(lp, rp)
    max_power = temp_power if max_power < temp_power else max_power
    if lp < rp:
        left += 1
    else:
        right -= 1

print(max_power)
