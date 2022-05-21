S, M, L = [int(input()) for _ in range(3)]
print('happy' if S + M * 2 + L * 3 >= 10 else 'sad')
