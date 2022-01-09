dij = [0, -1, 0, 1, 0]
check_arr = [0] * 26


def dfs(c, y, x):
    if c == 26:
        return c
    max_c = c
    for k in range(4):
        ny, nx = y + dij[k], x + dij[k + 1]
        if 0 <= ny < R and 0 <= nx < C:
            ch = data[ny][nx]
            if check_arr[ch] == 0:
                check_arr[ch] = 1
                max_c = max(dfs(c + 1, ny, nx), max_c)
                if max_c == 26:
                    return max_c
                check_arr[ch] = 0
    return max_c


R, C = map(int, input().split())
data = []
for i in range(R):
    row = input()
    decoded_row = [''] * C
    for idx, char in enumerate(row):
        decoded_row[idx] = ord(char) - 65
    data.append(decoded_row)

check_arr[data[0][0]] = 1
print(dfs(1, 0, 0))
