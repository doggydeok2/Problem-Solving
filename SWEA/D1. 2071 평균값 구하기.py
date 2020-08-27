T = int(input())

for test_case in range(1, T + 1):
    inputs = list(map(int, input().split()))
    print(f'#{test_case} {int(round(sum(inputs) / len(inputs), 0))}')