while True:
    a, b = map(int, input().split())
    if not a:
        break
    else:
        if a > b and not a % b:
            print('multiple')
        elif a < b and not b % a:
            print('factor')
        else:
            print('neither')
