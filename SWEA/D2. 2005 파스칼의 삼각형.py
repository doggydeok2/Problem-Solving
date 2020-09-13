import math

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case}')
    for i in range(N):
        for j in range(i + 1):
            print(math.factorial(i) // (math.factorial(j) * math.factorial(i - j)), end = ' ')
        print('')