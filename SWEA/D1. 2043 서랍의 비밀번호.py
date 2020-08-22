P, K = map(int, input().split())
count = 0

for num in range(K, 1000):
    count += 1
    if P == num:
        print(count)
        break