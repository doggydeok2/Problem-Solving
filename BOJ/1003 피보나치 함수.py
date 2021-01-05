T = int(input())
fibo0, fibo1 = [0] * 41, [0] * 41
fibo0[0] = fibo1[1] = 1
for tc in range(T):
    N = int(input())
    if not fibo0[N] and N:
        for i in range(2, N + 1):
            if not fibo0[i]:
                fibo0[i] = fibo0[i - 2] + fibo0[i - 1]
                fibo1[i] = fibo1[i - 2] + fibo1[i - 1]
    print(fibo0[N], fibo1[N])
