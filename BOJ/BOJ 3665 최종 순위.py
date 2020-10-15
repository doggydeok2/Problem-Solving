T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ti = list(map(int, input().split()))
    M = int(input())
    # 자신보다 상위 랭크의 숫자를 표시할 리스트
    higherList = [[0] * (N + 1) for _ in range(N + 1)] 
    higherList[0][0] = N  # 이후 리스트 사용에 문제가 없게끔 0행 0열에 큰 값을 입력

    for r in range(N):  # rank를 순회하며, (ti 리스트 순회에 사용)
        for j in range(1, N + 1):  # 0번 열을 visited로 사용
            higherList[ti[r]][0] = 1  # 방문 표시
            if not higherList[j][0]:  # 방문 표시가 되어있지 않다면, 나보다 하위 랭크의 숫자
                higherList[j][ti[r]] = 1  # 따라서 내가 너보다 상위 숫자임을 표시
                higherList[0][ti[r]] += 1  # 0번 행을 하위 rank 숫자 counter로 사용

    for _ in range(M):  # 상대적인 등수가 바뀐 쌍의 수만큼 반복
        a, b = map(int, input().split())
        # 리스트에서 서로 간 상위, 하위 표시를 swap
        higherList[a][b], higherList[b][a] = higherList[b][a], higherList[a][b]
        if higherList[a][b]:  # 카운팅도 변경: 1이 됐다면 a가 b보다 하위 rank가 된 것
            higherList[0][b] += 1
            higherList[0][a] -= 1
        else:  # 반대의 경우, a가 b보다 상위 랭크가 됨
            higherList[0][a] += 1
            higherList[0][b] -= 1

    for i in range(N + 1):  # sorting
        higherList[0][i] = [higherList[0][i], i]  # 카운트 옆에 팀 번호를 기입
    higherList[0].sort()  # 정렬하면 최하위 rank 팀부터 순서대로 정렬됨

    flagPossible = 1  # 가능한 테스트 케이스인지 확인하기 위한 flag
    for i in range(N):  # 하위 rank 수가 같다면 같은 순번의 숫자란 뜻: 불가능한 경우
        if higherList[0][i][0] == higherList[0][i + 1][0]: flagPossible = 0

    if not flagPossible:
        print("IMPOSSIBLE")  # 불가능한 테스트 케이스의 경우 출력
    else:
        for i in range(N - 1, -1, -1):  # 가능한 테스트의 경우, 상위 rank부터 순서대로 출력
            print(higherList[0][i][1], end = ' ')
        print()