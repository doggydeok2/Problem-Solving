def check(_l):
    for i in range(2, _l):
        if stack[-i] != bomb[-i]:
            return False
    return True


string, bomb = input(), input()
lb = len(bomb)
stack = []

for idx, ch in enumerate(string):
    stack.append(ch)
    if len(stack) >= lb and ch == bomb[-1] and check(lb + 1):
        for i in range(lb):
            stack.pop()
print(''.join(stack) if stack else 'FRULA')
