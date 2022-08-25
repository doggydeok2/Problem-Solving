DP = [0] * 1001
DP[2] = 1
for i in range(3, 1001):
    DP[i] = DP[i - 1] * 2 + (-1) ** i
while True:
    try:
        print(DP[int(input())])
    except:
        break
