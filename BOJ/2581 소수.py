M, N = int(input()), int(input())
minPrime = total = 0
for i in range(M, N + 1):
    if i == 1: continue
    flag = 1
    for j in range(2, i // 2 + 1):
        if not i % j:
            flag = 0
            break
    if flag:
        total += i
        if not minPrime: minPrime = i
if total:
    print(total)
    print(minPrime)
else:
    print(-1)