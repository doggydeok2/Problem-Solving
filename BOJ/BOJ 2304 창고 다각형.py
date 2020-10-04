N = int(input())
Arr = [0] * 10000
HMax, HMax2, total = 0, 0, 0
for _ in range(N):
    L, H = map(int, input().split())
    Arr[L] = H

for i in range(10000):
    if Arr[i] > HMax: HMax = Arr[i]
    total += HMax
    if Arr[9999 - i] > HMax2: HMax2 = Arr[9999 - i]
    total += HMax2

total -= HMax * 10000
print(total)