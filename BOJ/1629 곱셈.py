A, B, C = map(int, input().split())
B = bin(B)[2:]
lB = len(B)
acc = [0] * lB
acc[0] = A

for n in range(1, lB):
    acc[n] = acc[n - 1] ** 2 % C

total = 1
for x in range(lB - 1, -1, -1):
    if B[x] == '1':
        total *= acc[lB - 1 - x] % C

print(total % C)
