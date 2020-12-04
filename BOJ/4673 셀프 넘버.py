def self_number(n):
    return n + n % 10 + n % 100 // 10 +  n % 1000 // 100 + n // 1000


cntArr = [0] * 10001
for i in range(1, 9976):
    N = self_number(i)
    if N <= 10000: cntArr[N] = 1

for i in range(1, 10001):
    if not cntArr[i]: print(i)