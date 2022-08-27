for _ in range(int(input())):
    N = (int(input()) - 1) % 28 + 1
    print(''.join(['딸기' if (N if N < 16 else 30 - N) & (1 << (3 - i)) else 'V' for i in range(4)]))
