S = int(input())
switch = [3] + list(map(int, input().split()))
N = int(input())

for _ in range(N):
    G, P = map(int, input().split())
    if G == 1:
        for i in range(P, S + 1, P):
            switch[i] = 1 if switch[i] == 0 else 0
    else:
        switch[P] = 1 if switch[P] == 0 else 0
        i = 1
        while 1 <= P + i <= S and 1 <= P - i <= S:
            if switch[P + i] == switch[P - i]:
                switch[P + i] = 1 if switch[P + i] == 0 else 0
                switch[P - i] = 1 if switch[P - i] == 0 else 0
                i += 1
            else: break

for i in range(1, S + 1, 20):
    for j in range(i, min(i + 20, S + 1)):
        print(switch[j], end = ' ')
    print()