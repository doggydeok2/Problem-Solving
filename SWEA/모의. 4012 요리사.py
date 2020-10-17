def syn(n, k):  # n: 현재 수, k: sy1이 가져간 시너지 수
    global gapMin
    if k == N // 2 or n - k > N // 2:  # sy1이나 sy2 중 하나가 다 찼을 때,
        if k == N // 2:  # sy1이 먼저 다 찬 경우
            sn = n
            for x in range(n - k - 1, N // 2):  # sy2의 남은 공간에 나머지 수를 다 채운다
                sy2[x] = sn
                sn += 1
        else:  # sy2가 먼저 다 찬 경우
            sn = n
            for x in range(n - N // 2 - 1, N // 2):  # sy1의 남은 공간에 나머지 수를 다 채운다
                sy1[x] = sn
                sn += 1

        gap = 0
        for j in sy1:
            for i in sy1:  # sy1의 시너지를 gap에 모두 더하고
                gap += syns[j - 1][i - 1]
        for j in sy2:
            for i in sy2:  # sy2의 시너지를 gap에 모두 빼 두 음식 간 시너지 차이를 구한다
                gap -= syns[j - 1][i - 1]
        gapMin = abs(gap) if abs(gap) < gapMin else gapMin  # 음식 간 시너지 최소를 갱신한다

    else:  # 다 차지 않았다면 subset을 진행
        sy2[n - k - 1] = n
        syn(n + 1, k)
        sy2[n - k - 1] = 0
        sy1[k] = n
        syn(n + 1, k + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    syns = [list(map(int, input().split())) for _ in range(N)]
    gapMin = 2000000
    sy1, sy2 = [0] * (N // 2), [0] * (N // 2)  # 시너지의 절반 크기를 갖는 두 개의 리스트 선언

    syn(1, 0)

    print(f'#{tc} {gapMin}')