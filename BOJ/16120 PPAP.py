def ppap_check():
    a_flag = False
    for ch in string:
        if a_flag:
            if ch == 'A':
                return 'NP'
            stack.pop()
            if len(stack) >= 2 and stack[-1] == stack[-2] == 'P':
                stack.pop()
                stack.pop()
            else:
                stack.append('A')
        a_flag = False
        stack.append(ch)
        if ch == 'A':
            a_flag = True
    return 'PPAP' if len(stack) == 1 and stack[-1] == 'P' else 'NP'


string = input()
stack = []
print(ppap_check())
