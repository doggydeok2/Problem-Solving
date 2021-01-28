T = int(input())
for tc in range(T):
    N, target = map(int, input().split())
    Q = list(map(int, input().split()))

    cnt = 0
    while True:
        maxN = maxIdx = 0
        for i in range(N - cnt):
            if Q[i] > maxN:
                maxN = Q[i]
                maxIdx = i
        if target == maxIdx:
            break
        Q = Q[maxIdx + 1:] + Q[:maxIdx]
        target += N - cnt - maxIdx - 1 if maxIdx > target else - maxIdx - 1
        cnt += 1
    print(cnt + 1)
