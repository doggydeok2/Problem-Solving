fibo = [0] * 10001
fibo[0] = fibo[1] = fibo[2] = 1
idx = 3

T = int(input())
for tc in range(1, T + 1):
    P, Q = map(int, input().split())

    if not fibo[P]:
        for i in range(idx, P + 1):
            fibo[i] = fibo[i - 1] + fibo[i - 2]
            idx += 1
    print(f'Case #{tc}: {fibo[P] % Q}')