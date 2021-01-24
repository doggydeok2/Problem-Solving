T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    total = 1
    for i in range(min(N, M - N)):
        total *= M - i
        total //= i + 1
    print(total)