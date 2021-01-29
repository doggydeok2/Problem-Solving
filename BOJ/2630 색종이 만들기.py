def is_square(y, x, n):
    global B, W
    if n == 1:
        if sq[y][x]:
            B += 1
        else:
            W += 1
    else:
        flag = 0
        for i in range(y, y + n):
            for j in range(x, x + n):
                if sq[i][j] != sq[y][x]:
                    flag = 1
                    break
            if flag:
                is_square(y, x, n // 2)
                is_square(y, x + n // 2, n // 2)
                is_square(y + n // 2, x, n // 2)
                is_square(y + n // 2, x + n // 2, n // 2)
                break
        if not flag:
            if sq[y][x]:
                B += 1
            else:
                W += 1


N = int(input())
sq = [list(map(int, input().split())) for _ in range(N)]
B = W = 0
is_square(0, 0, N)
print(W)
print(B)
