M, N = int(input()), int(input())
squares = [i ** 2 for i in range(int(M ** 0.5) + 1 - (int(M ** 0.5) ** 2 == M), int(N ** 0.5) + 1)]
print(f'{sum(squares)}\n{squares[0]}' if len(squares) else -1)
