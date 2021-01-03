import sys
input = sys.stdin.readline
cntArr = [0 for i in range(10001)]
for i in range(int(input())):
    cntArr[int(input())] += 1
for i in range(1, 10001):
    for n in range(cntArr[i]):
        print(i)