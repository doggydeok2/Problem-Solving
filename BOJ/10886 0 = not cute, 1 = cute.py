N = int(input())
print(f'Junhee is {"" if sorted([int(input()) for _ in range(N)])[N // 2] == 1 else "not "}cute!')
