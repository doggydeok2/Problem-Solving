T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]
    DP_arr = [0, 0, score[0][0], score[1][0]] + [0] * (2 * n - 2)

    for i in range(1, n):
        DP_arr[2 * i + 2] = max(DP_arr[2 * i + 1], DP_arr[2 * i - 1]) + score[0][i]
        DP_arr[2 * i + 3] = max(DP_arr[2 * i], DP_arr[2 * i - 2]) + score[1][i]

    print(max(DP_arr[-1], DP_arr[-2]))
