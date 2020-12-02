for tc in range(1, int(input()) + 1):
    results = input()
    total, pt = 0, 1
    
    for result in results:
        if result == 'O':
            total += pt
            pt += 1
        else:
            pt = 1
    print(total)