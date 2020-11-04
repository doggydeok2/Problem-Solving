for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    adl = [[] for _ in range(N + 1)]
    v = [0] * (N + 1)
    v[0] = v[1] = 1
    for _ in range(M):
        a, b = map(int, input().split())
        adl[a].append(b)
        adl[b].append(a)
 
    Q = []
    r = 0
    for f in adl[1]:
        Q.append(adl[f])
        r += 1
        v[f] = 1
     
    cnt = r
    for i in range(r):
        for f in Q[i]:
            if not v[f]:
                cnt += 1
                v[f] = 1
    print(f'#{tc} {cnt}')