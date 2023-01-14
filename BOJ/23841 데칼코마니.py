N, M = map(int, input().split())
for _ in range(N):
    r = list(input())
    print(''.join([r[M - 1 - i] if r[M - 1 - i] != '.' else r[i] for i in range(M)]))
