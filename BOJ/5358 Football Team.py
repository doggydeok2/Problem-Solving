try:
    while True:
        name = list(input())
        for i, ch in enumerate(name):
            if ch == 'i':
                name[i] = 'e'
            elif ch == 'e':
                name[i] = 'i'
            elif ch == 'I':
                name[i] = 'E'
            elif ch == 'E':
                name[i] = 'I'
        print(''.join(name))
except:
    pass
