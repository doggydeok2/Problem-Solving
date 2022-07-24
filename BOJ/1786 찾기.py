T, P = input(), input()
pi_table = [0] * (len(P) + 1)

pi_table[-1], j = -1, 0
for i in range(1, len(P)):
    while j >= 0 and P[i] != P[j]:
        j = pi_table[j - 1]
    j += 1
    pi_table[i] = j

indexes, j = [], 0
for i in range(len(T)):
    while j >= 0 and T[i] != P[j]:
        j = pi_table[j - 1]
    j += 1
    if j == len(P):
        indexes.append(i - j + 2)
        j = pi_table[j - 1]

print(len(indexes))
print(*indexes)
