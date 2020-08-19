N = int(input())

for num in range(1, 1001):
    if N % num == 0:
        print(num, end = ' ')