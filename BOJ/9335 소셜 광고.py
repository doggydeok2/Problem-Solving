def brute_force(n, k):
    global minAd
    if n == N or k >= minAd:
        return
    else:
        flag = 1
        brute_force(n + 1, k)
        cntArr[n + 1] += 1
        for i in range(1, adl[n][0] + 1):
            cntArr[adl[n][i]] += 1
        for watched in cntArr:
            if not watched:
                flag = 0
                break
        if flag:
            minAd = min(minAd, k + 1)
        else:
            brute_force(n + 1, k + 1)
        cntArr[n + 1] -= 1
        for i in range(1, adl[n][0] + 1):
            cntArr[adl[n][i]] -= 1


T = int(input())
for tc in range(T):
    N = int(input())
    adl = [list(map(int, input().split())) for _ in range(N)]
    cntArr = [0] * (N + 1)
    cntArr[0] = 1
    minAd = N
    brute_force(0, 0)
    print(minAd)
