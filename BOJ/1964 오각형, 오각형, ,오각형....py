N = int(input())
dots = [1 + 3 * i for i in range(N + 1)]
acc = [0] * (N + 1)
for i in range(N + 1):
    acc[i] = (acc[i - 1] + dots[i]) % 45678
print(acc[-1])
