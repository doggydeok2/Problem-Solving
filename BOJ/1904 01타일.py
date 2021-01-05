N = int(input())
ables = [0] * 3
ables[1], ables[2] = 1, 2
for i in range(3, N + 1):
    ables[i % 3] = (ables[(i + 1) % 3] + ables[(i + 2) % 3]) % 15746
print(ables[N % 3])