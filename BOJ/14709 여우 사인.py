N = int(input())
adj = [[0] * 6 for _ in range(6)]
for i in range(N):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1

if N == 3 and adj[1][3] and adj[1][4] and adj[3][4]:
    print('Wa-pa-pa-pa-pa-pa-pow!')
else:
    print('Woof-meow-tweet-squeek')
