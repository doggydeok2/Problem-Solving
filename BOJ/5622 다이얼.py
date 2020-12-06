ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numArr = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7]
S = input()
total = 0
for ch in S:
    for i in range(26):
        if ch == ABC[i]:
            total += 3 + numArr[i]
print(total)