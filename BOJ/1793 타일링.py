DP = [0] * 251
DP[0], DP[1], DP[2] = 1, 1, 3
ptr = 3

while True:
    try:
        n = int(input())
        for i in range(ptr, n + 1):
            DP[i] = DP[i - 1] + 2 * DP[i - 2]
        ptr = n if ptr < n else ptr
        print(DP[n])
    except EOFError:
        break
