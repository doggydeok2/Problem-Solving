T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N + 1)]
    ans = 0

    for j in range(N):
        cntX, cntY = 0, 0
        for i in range(N + 1):
            if puzzle[j][i]:
                cntX += 1
            else:
                if cntX == K:
                    ans += 1
                cntX = 0

            if puzzle[i][j]:
                cntY += 1
            else:
                if cntY == K:
                    ans += 1
                cntY = 0
    print(f'#{tc} {ans}')

