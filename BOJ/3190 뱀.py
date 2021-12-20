import collections


dij = [0, -1, 0, 1, 0]  # +1: L, -1: D
N, K = int(input()), int(input())
board = [[0] * N for _ in range(N)]
board[0][0] = 1
cnt, k = 0, 3
snake = collections.deque([(0, 0)])

for _ in range(K):
    r, c = map(int, input().split())
    board[r - 1][c - 1] = 2  # apple

L = int(input())
changes = collections.deque()
for _ in range(L):
    X, C = input().split()
    changes.append((int(X), C))

while True:
    cnt += 1
    x, y = snake[0]
    nx, ny = x + dij[k], y + dij[k + 1]
    if 0 <= nx < N and 0 <= ny < N and board[ny][nx] != 1:
        if board[ny][nx] == 0:
            popped_x, popped_y = snake.pop()
            board[popped_y][popped_x] = 0
        board[ny][nx] = 1
        snake.appendleft((nx, ny))
    else:
        break

    if changes and changes[0][0] == cnt:
        change_time, change_direction = changes.popleft()
        k = (k + 1) % 4 if change_direction == 'L' else (k + 3) % 4

print(cnt)
