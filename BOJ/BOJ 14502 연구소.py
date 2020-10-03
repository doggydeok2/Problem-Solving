di = [-1, 0, 1, 0]  # 사방 탐색용 i좌표
dj = [0, -1, 0, 1]  # 사방 탐색용 j좌표


def bfs(stage, j, i):  # BFS
    q = [0] * M * N  # 큐는 맵의 크기만큼 선언
    q[0] = [j, i]  # 큐는 매개 변수로 받은 바이러스 좌표로 초기화
    ptr, turn = 1, 0  # 포인터, 차례 초기화
    while ptr > turn:  # 큐가 빌 때까지 반복
        y, x = q[turn][0], q[turn][1]  # 좌표를 y, x에 나눠담고
        for k in range(4):  # 사방에 걸쳐 확인
            cal_y, cal_x = y + dj[k], x + di[k]
						# 바이러스 옆에 있고 계산한 좌표가 안전지대면
            if 0 <= cal_y < N and 0 <= cal_x < M and not stage[cal_y][cal_x]:
                stage[cal_y][cal_x] = 3  # 해당 지역이 바이러스로 감염된 안전지대임을 표시
                q[ptr] = [cal_y, cal_x]  # 이 지역을 큐에 추가
                ptr += 1  # 포인터 증가
        turn += 1  # 사방 계산이 끝났으면 큐의 다음 값을 꺼내기 위해 차례 증가


def bruteforce(y, x, k):  # 완전 탐색
    global cntMax
    if k == 3:  # 벽을 세 개 세웠을 경우
        for j in range(N):  # 맵을 순회하며
            for i in range(M):
                if data[j][i] == 2:  # 바이러스를 찾은 경우 BFS 진행
                    bfs(data, j, i)

        cnt = 0  # 안전지대를 셀 카운터 선언
        for j in range(N):  # 맵을 순회하며
            for i in range(M):
                if not data[j][i]:  # 안전지대일 경우
                    cnt += 1  # 카운터 증가
                elif data[j][i] == 3:  # 바이러스에 의해 감염된 지역일 경우
                    data[j][i] = 0  # 빈 공간으로 만들어줌
        if cntMax < cnt:  # 이번 회차에 구한 안전지대의 수가 최대값인 경우
            cntMax = cnt  # 안전지대의 최대치를 갱신
    else:  # 벽을 다 세우지 않았다면
        for j in range(y, N):  # 벽을 중복 없이 셋 세움: 맵을 순회하며
            if not j == y:  # 좌표 정리
                x = 0
            for i in range(x, M):
                if not data[j][i] and k != 3:  # 빈 공간이고 벽을 셋 세우지 않았다면
                    data[j][i] = 1  # 벽을 세우고
                    bruteforce(j, i, k + 1)  # 다음 벽을 세우기 위한 완전탐색 진행
                    data[j][i] = 0  # 벽을 치움


N, M = map(int, input().split())  # 세로 크기 N, 가로 크기 M
data = [list(map(int, input().split())) for _ in range(N)]  # 지도 모양: 0 빈 칸, 1 벽, 2 바이러스
cntMax = 0  # 안전 지대의 최대치
bruteforce(0, 0, 0)  # 완전 탐색
print(cntMax)  # 결과 출력