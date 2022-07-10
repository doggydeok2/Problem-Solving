import sys
rl = sys.stdin.readline


def cal_fibo(_n):
    if _n == 1:
        return [1, 1, 1, 0]
    else:
        a, b, c, d = cal_fibo(_n // 2)
        a, b, c, d = (a ** 2 + b * c) % MOD, (a * b + b * d) % MOD, (a * c + c * d) % MOD, (b * c + d ** 2) % MOD
        if _n % 2:
            a, b, c, d = (a + b) % MOD, a, (c + d) % MOD, c
        return [a, b, c, d]


def get_fibo(_n):
    if _n == 0:
        return 0
    elif _n == 1:
        return 1
    return cal_fibo(_n - 1)[0]


MOD = 10000
while True:
    n = int(rl())
    if n == -1:
        break
    print(get_fibo(n))
