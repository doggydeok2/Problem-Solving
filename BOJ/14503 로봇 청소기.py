dij = [-1, 0, 1, 0, -1]  # 북, 동, 남, 서


def cleaning(i, j, direction):
    cnt = 0
    while True:
        if not visited[i][j]:
            cnt += 1
            visited[i][j] = 1

        clean_disable_check = 0
        for k in range(1, 5):
            td = (direction + 4 - k) % 4
            ti = i + dij[td]
            tj = j + dij[td + 1]
            if 0 <= ti < N and 0 <= tj < M and not position[ti][tj] and not visited[ti][tj]:
                i, j, direction = ti, tj, td
                break
            clean_disable_check += 1

        if clean_disable_check == 4:
            bi, bj = i + dij[(direction + 2) % 4], j + dij[(direction + 2) % 4 + 1]
            if position[bi][bj]:
                return cnt
            else:
                i, j = bi, bj


N, M = map(int, input().split())
r, c, d = map(int, input().split())
position = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
print(cleaning(r, c, d))
