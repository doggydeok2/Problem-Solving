dij = [-1, 0, 1, 0, -1]


# BFS 와 DFS 를 모두 진행
def bdfs(n, x, y, arr):  # n: 구슬 발사 횟수, x, y: 벽돌 좌표, arr: 게임판의 복사본
    global cntMin
    if n == N:  # 공을 모두 발사한 경우
        cnt = 0
        for x in range(W):  # 각 열별로 남은 벽돌의 수를 카운팅
            cnt_y = H  # 열의 벽돌 수는 높이로 초기화
            for y in range(H):  # 열의 각 행을 탐색하며
                if not arr[y][x]:  # 벽돌이 없다면
                    cnt_y -= 1  # 벽돌 수를 하나씩 줄임
                else:  # 첫 블럭을 만난 순간
                    cnt += cnt_y  # 그 열의 블럭 수를 카운터에 더해주고 반복문 탈출
                    break
        cntMin = cnt if cntMin > cnt else cntMin  # 블럭 수의 최소값 갱신
    else:  # 발사할 공이 남았다면
        q = [(0, 0, 0)] * (W * H)  # 큐 초기화
        q[0] = (y, x, arr[y][x])  # 큐에 매개변수로 받은 좌표와, 벽돌의 수를 입력
        arr[y][x] = 0  # 첫 좌표의 벽돌을 치움
        ptr, turn = 1, 0
        flag = 1  # 벽돌이 하나도 남지 않았을 경우를 대비한 플래그

        while ptr != turn:  # BFS
            ty, tx = q[turn][0], q[turn][1]  # 큐에서 좌표를 꺼내
            for d in range(1, q[turn][2]):  # 벽돌에 적혀있던 수만큼
                for k in range(4):  # 상하좌우 4방향으로 BFS 진행
                    cal_y, cal_x = ty + (d * dij[k + 1]), tx + (d * dij[k])  # 좌표 계산
                    if 0 <= cal_x < W and 0 <= cal_y < H:  # 계산한 좌표가 유효하고
                        if arr[cal_y][cal_x]:  # 해당 좌표에 벽돌이 있으면
                            q[ptr] = (cal_y, cal_x, arr[cal_y][cal_x])  # 큐에 추가
                            arr[cal_y][cal_x] = 0  # 좌표의 벽돌을 치움
                            ptr += 1
            turn += 1

        # 열별로 블록 수를 세어 하단부터 정렬
        for x in range(W):  # 열만큼 반복
            for k in range(H, 0, -1):  # 각 열에 대하여 하단부터 버블 소트
                for y in range(1, k):
                    if arr[y - 1][x] and not arr[y][x]:
                        arr[y - 1][x], arr[y][x] = arr[y][x], arr[y - 1][x]
        # DFS
        for x in range(W):  # 각 열에 대해
            for y in range(H):  # 행을 확인하며
                if arr[y][x]:  # 벽돌이 남아 있으면
                    flag = 0  # 벽돌이 남아있었음을 플래그에 표시하고
                    bdfs(n + 1, x, y, [arr[_][:] for _ in range(H)])  # 재귀
                    break  # 재귀 이후엔 다음 열로 이동

        if flag:  # 벽돌이 하나도 없어 DFS 를 진행할 수 없었다면
            cntMin = 0  # 남은 벽돌이 없으니 카운터도 0


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]
    cntMin = 180

    for i in range(W):  # 1번 공: 각 열을 순회하며
        for j in range(H):  # 해당 열의 각 행을 순회하여
            if data[j][i]:  # 벽돌이 있다면
                # 해당 좌표와 게임판 복사본을 함수의 전달인자로 함수 실행
                bdfs(0, i, j, [data[_][:] for _ in range(H)])
                break  # 함수 실행 이후엔 다음 열로 이동

    print(f'#{tc} {cntMin}')  # 벽돌의 최소 수 출력
