import itertools


def dfs(y, x, direction):
    ny, nx = y + dij[direction], x + dij[direction + 1]
    if 0 <= ny < N and 0 <= nx < N and data[ny][nx] != 'O':
        if data[ny][nx] == 'S':
            return True
        else:
            return dfs(ny, nx, direction)
    else:
        return False


dij = [0, -1, 0, 1, 0]
N = int(input())
data, teachers, blanks = [], [], []
avoidable = True

for r in range(N):
    row = list(input().split())
    data.append(row)
    for c in range(N):
        if row[c] == 'X':
            blanks.append((r, c))
        elif row[c] == 'T':
            teachers.append((r, c))
        # else do nothing

for covers in itertools.combinations(blanks, 3):
    avoidable = True
    for cover in covers:
        r, c = cover
        data[r][c] = 'O'

    for teacher in teachers:
        r, c = teacher
        for k in range(4):
            if dfs(r, c, k):
                avoidable = False
                break
        if not avoidable:
            break

    if avoidable:
        break

    for cover in covers:
        r, c = cover
        data[r][c] = 'X'

print('YES' if avoidable else 'NO')
