def baby_gin():
    one, two = [0] * 10, [0] * 10
    ptr = 0

    for i in range(6):
        one[nums[2 * i]] += 1
        if i >= 2:
            for x in range(10):
                if one[x] > 2: return 1
                elif x > 1 and one[x] and one[x - 1] and one[x - 2]: return 1
        two[nums[2 * i + 1]] += 1
        if i >= 2:
            for x in range(10):
                if two[x] > 2: return 2
                elif x > 1 and two[x] and two[x - 1] and two[x - 2]: return 2
    return 0


T = int(input())
for tc in range(1, T + 1):
    nums = list(map(int, input().split()))
    print(f'#{tc} {baby_gin()}')
