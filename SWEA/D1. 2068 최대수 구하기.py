for test_case in range(1, T + 1):
    inputs = list(map(int, input().split()))
    max = 0
    for number in inputs:
        if max < number:
            max = number
    print(f'#{test_case} {max}')