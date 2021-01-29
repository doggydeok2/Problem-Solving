def counting(num):
    global m, z, p
    if num == -1:
        m += 1
    elif num:
        p += 1
    else:
        z += 1


def dnc(y, x, n):
    global m, z, p
    if n == 1:
        counting(paper[y][x])
    else:
        flag = 0
        for i in range(y, y + n):
            for j in range(x, x + n):
                if paper[y][x] != paper[i][j]:
                    flag = 1
                    break
            if flag:
                break
        if flag:
            for i in range(y, y + n, n // 3):
                for j in range(x, x + n, n // 3):
                    dnc(i, j, n // 3)
        else:
            counting(paper[y][x])


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
m = z = p = 0

dnc(0, 0, N)
print(m)
print(z)
print(p)