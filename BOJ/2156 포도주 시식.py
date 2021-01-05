n = int(input())
if n == 1:
    print(int(input()))
elif n == 2:
    print(int(input()) + int(input()))
else:
    wines = [[0, 0] for _ in range(n)]

    wines[0][0] = wines[0][1] = int(input())
    wines[1][0] = int(input())
    wines[1][1] = wines[0][0] + wines[1][0]
    wines[2][0] = wines[2][1] = int(input())
    wines[2][0] += wines[0][0]
    wines[2][1] += wines[1][0]

    for i in range(3, n):
        wine = int(input())
        wines[i][0] = max(wines[i - 2][0], wines[i - 2][1], wines[i - 3][1]) + wine
        wines[i][1] = wines[i - 1][0] + wine

    print(max(wines[-1][0], wines[-1][1], wines[-2][1]))
