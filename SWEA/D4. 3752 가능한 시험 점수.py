T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))  # 입력받은 문제 배점
    chkArr, totals = [0] * 10001, [0] * N ** 2  # 점수는 최대 1만점, 가짓수는 N²개
    ptr = 1  # totals에 값 기입 시 사용할 포인터

    for score in scores:  # 점수를 순회하며
        for i in range(ptr):  # 현재 존재하는 점수 합들을 훑어
            if not chkArr[score + totals[i]]:  # 새로운 점수 총합이 나왔다면
                chkArr[score + totals[i]] = 1  # DP에 표시하고
                totals[ptr] = score + totals[i]  # totals 에도 새 점수를 기입하고
                ptr += 1  # 포인터를 다음 칸으로 옮긴다

    print(f'#{tc} {ptr}')  # 포인터의 값이 곧 점수의 가짓수가 된다