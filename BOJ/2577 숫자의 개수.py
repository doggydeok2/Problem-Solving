A = int(input())
B = int(input())
C = int(input())
res = str(A * B * C)
cntArr = [0] * 10
for ch in res:
    cntArr[int(ch)] += 1
for cnt in cntArr:
    print(cnt)