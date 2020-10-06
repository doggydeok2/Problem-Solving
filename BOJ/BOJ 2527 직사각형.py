for _ in range(4):
    i = list(map(int, input().split()))

    if i[2] < i[4] or i[0] > i[6] or i[3] < i[5] or i[1] > i[7]:
        print('d')
    elif i[2] == i[4] and i[3] == i[5] or i[0] == i[6] and i[1] == i[7] or i[0] == i[6] and i[3] == i[5] or i[2] == i[4] and i[1] == i[7]:
        print('c')
    elif i[3] == i[5] or i[1] == i[7] or i[2] == i[4] or i[6] == i[0]:
        print('b')
    else:
        print('a')
