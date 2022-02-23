formula = input()
nums = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
ops = ['+', '-', 'x', '/', '=']
for idx, num in enumerate(nums):
    formula = formula.replace(num, str(idx))
splits = []
i = 0
for idx, ch in enumerate(formula):
    if ch in ops:
        splits.append(formula[i:idx])
        splits.append(ch)
        i = idx + 1
try:
    cal = int(splits[0])
    for i in range(1, len(splits) - 1, 2):
        if splits[i] == '+':
            cal += int(splits[i + 1])
        elif splits[i] == '-':
            cal -= int(splits[i + 1])
        elif splits[i] == 'x':
            cal *= int(splits[i + 1])
        elif splits[i] == '/':
            if cal < 0:
                cal = -(-cal // int(splits[i + 1]))
            else:
                cal //= int(splits[i + 1])
        else:
            raise ValueError

    ans = ''
    for ch in str(cal):
        ans += '-' if ch == '-' else nums[int(ch)]
    print(formula)
    print(ans)
except:
    print('Madness!')
