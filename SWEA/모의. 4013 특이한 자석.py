def rotate(n):
    if 0 <= n - 1 < 4 and magnets[n - 1][ptrs[n - 1][1]] != magnets[n][ptrs[n][0]] and not chk[n - 1]:
        chk[n - 1] = 1
        rotate(n - 1)
    if 0 <= n + 1 < 4 and magnets[n][ptrs[n][1]] != magnets[n + 1][ptrs[n + 1][0]] and not chk[n + 1]:
        chk[n + 1] = 1
        rotate(n + 1)


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]  # 0: 점수, 2 and 6: 우/좌측 자성비교
    ptrs = [[6, 2], [6, 2], [6, 2], [6, 2]]
    chk = [0, 0, 0, 0]
    total = 0

    for _ in range(K):
        N, W = map(int, input().split())
        chk[N - 1] = 1
        rotate(N - 1)
        for i in range(4):
            if chk[i]:
                if N % 2 != i % 2:
                    ptrs[i][0] = (ptrs[i][0] - W + 8) % 8
                    ptrs[i][1] = (ptrs[i][1] - W + 8) % 8
                else:
                    ptrs[i][0] = (ptrs[i][0] + W + 8) % 8
                    ptrs[i][1] = (ptrs[i][1] + W + 8) % 8
                chk[i] = 0

    for i in range(4):
        score = 2 ** i
        if magnets[i][(ptrs[i][1] + 6) % 8]:
            total += score

    print(f'#{tc} {total}')
