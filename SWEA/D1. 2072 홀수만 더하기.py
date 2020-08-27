T = int(input())

for test_case in range(1, T + 1):
    inputs = list(map(int, input().split()))
    total = 0
    for scrab in inputs:
        total += scrab if scrab % 2 else 0
    print(f'#{test_case} {total}')