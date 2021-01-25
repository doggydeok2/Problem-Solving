while True:
    stack = []
    sen = input()
    if sen == '.':
        break
    flag = 1
    for i in range(len(sen)):
        if sen[i] == '(' or sen[i] == '[':
            stack.append(sen[i])
        elif sen[i] == ']':
            if not stack or stack.pop() != '[':
                flag = 0
                break
        elif sen[i] == ')':
            if not stack or stack.pop() != '(':
                flag = 0
                break
    print('yes' if flag and not stack else 'no')
