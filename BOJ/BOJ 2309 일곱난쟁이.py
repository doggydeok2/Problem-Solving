data = [0] * 9
chkArr = []
flag = 0

for i in range(9):
    data[i] = int(input())
sumH = sum(data) - 100

for i in range(0, 8):
    s = data[i]
    for j in range(i + 1, 9):
        s += data[j]
        if s == sumH:
            flag = 1
            chkArr = [i, j]
            break
        s -= data[j]
    if flag: break

for x in chkArr:
    data[x] = 0
data.sort()
for i in range(2, 9):
    print(data[i])