def quad_tree(y, x, n):
    global compress
    if n == 1:
        compress += origin[y][x]
    else:
        flag = 0
        for i in range(y, y + n):
            for j in range(x, x + n):
                if origin[y][x] != origin[i][j]:
                    flag = 1
                    break
            if flag:
                break
        if flag:
            compress += '('
            quad_tree(y, x, n // 2)
            quad_tree(y, x + n // 2, n // 2)
            quad_tree(y + n // 2, x, n // 2)
            quad_tree(y + n // 2, x + n // 2, n // 2)
            compress += ')'
        else:
            compress += origin[y][x]


N = int(input())
origin = [input() for _ in range(N)]
compress = ''

quad_tree(0, 0, N)
print(compress)
