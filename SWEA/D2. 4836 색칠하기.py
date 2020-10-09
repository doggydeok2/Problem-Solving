T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    paper =[[0 for _ in range(10)] for _ in range(10)]
    paint = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
 
    for lists in paint:
        for i in range(lists[0], lists[2] + 1):
            for j in range(lists[1], lists[3] + 1):
                if not paper[j][i] == lists[4]: paper[j][i] += lists[4]
    for colors in paper:
        for color in colors:
            if color >= 3: cnt += 1
    print(f'#{tc} {cnt}')