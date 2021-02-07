inversions = [0] + [[0] * 154 for _ in range(18)]
inversions[1][0] = inversions[2][0] = inversions[2][1] = 1
for i in range(3, 19):
    for j in range((i * i - i) // 2 + 1):
        inversions[i][j] = inversions[i - 1][j] + inversions[i][j - 1]
        if j >= i:
            inversions[i][j] -= inversions[i - 1][j - i]

while True:
    n, k = map(int, input().split())
    maxValue = n * (n - 1) // 2
    if not n and not k:
        break
    if k > maxValue:
        print(0)
    else:
        print(inversions[n][min(k, maxValue - k)])
