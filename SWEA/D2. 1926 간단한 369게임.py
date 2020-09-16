N = int(input())

for i in range(1, N + 1):
    isclab = False
    if i // 100 == 3 or i // 100 == 6 or i // 100 == 9:
        print('-', end = '')
        isclab = True
    if i % 100 // 10 == 3 or i % 100 // 10 == 6 or  i % 100 // 10 == 9:
        print('-', end = '')
        isclab = True
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print('-', end = '')
        isclab = True
    if not isclab:
        print(i, end = '')
    print(end = ' ')
    