def mul_dnc(a, b):
    if b == 0:
        return 1
    elif b % 2:
        return mul_dnc(a, b - 1) * a
    else:
        return (mul_dnc(a, b // 2) % p) ** 2 % p


N, K = map(int, input().split())
A = B = 1
p = 1000000007

for i in range(min(K, N - K)):
    A *= N - i
    A %= p
    B *= i + 1
    B %= p
B = mul_dnc(B, p - 2)
print(A * B % p)