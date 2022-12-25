for _ in range(int(input())):
    Y = K = 0
    for _ in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k
    print('Draw' if Y == K else ['Yonsei', 'Korea'][Y < K])
