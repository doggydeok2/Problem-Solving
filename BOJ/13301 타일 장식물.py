fibo = [0] * 83
fibo[1] = fibo[2] = 1
for i in range(3, 83):
    fibo[i] = fibo[i - 1] + fibo[i - 2]
N = int(input())
print(2 * (fibo[N] + fibo[N + 1]))
