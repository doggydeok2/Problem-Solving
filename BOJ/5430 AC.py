T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    nums = list(input()[1:-1].split(','))
    isReversed = 0
    f, r = 0, n - 1

    flag = 0
    for cmd in p:
        if cmd == 'R':
            isReversed = not isReversed
            f, r = r, f
        else:
            if not isReversed and r < f or isReversed and r > f:
                flag = 1
                break
            f -= 1 if isReversed else -1
    if flag:
        print('error')
    elif not isReversed and r < f or isReversed and r > f:
        print('[]')
    else:
        print('[', end='')
        if isReversed:
            for i in range(f, r, -1):
                print(nums[i], end=',')
            print(nums[r] + ']')
        else:
            for i in range(f, r):
                print(nums[i], end=',')
            print(nums[r] + ']')
