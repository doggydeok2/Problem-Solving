def solution(key, lock):
    M, N = len(key), len(lock)  # key와 lock의 한 변 길이를 변수로 초기화
    board = [[0] * (2 * M + N - 2) for _ in range(2 * M + N - 2)]  # 모든 케이스를 담을 수 있는 크기의 board 설정
    for i in range(N):  # board의 중앙에 lock 배치
        for j in range(N):
            board[M - 1 + j][M - 1 + i] = lock[j][i]

    # 모든 경우 탐색: 4 * (M + 2) ** 2회 반복
    for t in range(4):
        for i in range(M + 2):
            for j in range(M + 2):
                # 키 삽입
                ins(board, key, j, i, M, 1)
                # 자물쇠가 열렸는지 확인
                if op(board, key, M, N): return True  # 열렸다면  True를 반환
                # 키 제거
                ins(board, key, j, i, M, 0)
        # 키 회전
        keyTemp = [[0] * M for _ in range(M)]  # 임시 리스트 선언
        for j in range(M):  # 반복문을 통해 90도 회전된 키를 임시 리스트에 삽입
            for i in range(M):
                keyTemp[i][M - 1 - j] = key[j][i]
        key = keyTemp  # 원본 키에 덮어씌움
    if op(board, M, N): return True  # 처음부터 lock이 개방된 상태였는지 확인
    return False  # lock을 열 수 없다면 False를 반환


def ins(board, key, j, i, M, c):  # 키 삽입 함수
    if c == 1:  # 키를 삽입하는 경우
        for y in range(M):  # key 크기만큼 반복문을 돌며
            for x in range(M):
                board[j + y][i + x] += key[y][x]  # 보드에 key를 삽입
    else:  # 키를 제거하는 경우
        for y in range(M):  # key 크기만큼 반복문을 돌며
            for x in range(M):
                board[j + y][i + x] -= key[y][x]  # 보드에서 key를 제거


def op(board, M, N):  # lock의 개방 확인 함수
    for y in range(M - 1, M - 1 + N):  # 보드 중앙에서 lock 크기만큼 반복문을 돌며
        for x in range(M - 1, M - 1 + N):
            if board[y][x] == 1:  # 홈과 돌기가 만났다면
                continue  # 계속 확인
            else:  # 홈과 홈, 돌기와 돌기가 만났다면
                return 0  # 열 수 없음을 반환
    return 1  # 이상이 없다면 열 수 있음을 반환