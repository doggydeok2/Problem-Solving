for _ in range(int(input())):
    lt, wt, le, we = map(int, input().split())
    print('Eurecom' if le * we > lt * wt else 'Tie' if le * we == lt * wt else 'TelecomParisTech')
