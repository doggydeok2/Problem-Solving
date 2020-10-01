AtoN = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # 마약 공급책은 A부터 순서대로 알파벳 대문자 표현: 숫자로 변환할 때 참조할 str


def dfs(num):
    v[num] = 0  # num 번째의 client 는 더 이상 마약을 공급받지 못함
    # 이 dealer 가 공급하는 마약 중단
    for x in range(1, 27):  # 모든 경우의 수 확인
        if adj[num][x]:  # 이 dealer 가 마약을 공급하고 있었다면,
            adj[num][x] = 0  # 공급을 끊고,
            # 해당 client 가 다른 dealer 에게  마약을 공급받고 있는지 확인
            another = 0  # 공급책 확인용 flag
            for y in range(1, 27):  # 모든 경우의 수에 대해
                if adj[y][x]:  # 다른 공급책이 있다면
                    another = 1  # flag 전환 후 반복문 탈출
                    break
            if not another:
                dfs(x)  # 다른 공급책이 없다면, dfs 재귀 진행


adj = [[0] * 27 for _ in range(27)]  # 크기가 크지 않으므로, 나올 수 있는 N의 최대값만큼의 2차원 인접 배열 선언
v = [0] * 27  # 마약을 공급받고 있음을 표시하는 리스트 선언
N, M = map(int, input().split())  # N: 마약 공급책의 수, M: 마약 공급책의 관계 수
for _ in range(M):  # 마약 공급책의 관계 수만큼 반복
    d, c = input().split()  # d: 마약을 공급하는 dealer, c: 마약을 공급받는 client
    for i in range(1, 27):  # 알파벳 수만큼 반복
        # 인접 배열에 인덱스로 사용할 수 있도록 알파벳을 숫자로 변환함
        if d == AtoN[i]:
            d = i
        if c == AtoN[i]:
            c = i
    adj[d][c] = 1  # dealer d는 client c에게 마약을 공급함을 인접 배열에 표시
    v[c] = 1  # client c는 마약을 공급받는 상황임을 표시

arrest = list(input().split())  # 입력 마지막 줄: 마약 공급책의 수와 파악중인 각 마약 공급책
arrest[0] = int(arrest[0])  # 모든 입력을 str 형식으로 받았으니 수를 int 로 형변환
for i in range(1, 1 + arrest[0]):  # 파악중인 마약 공급책 수만큼 반복
    # 알파벳 입력을 인덱스로 사용할 수 있도록 숫자로 변환
    for j in range(1, 27):  # 알파벳 수만큼 반복
        if arrest[i] == AtoN[j]:
            arrest[i] = j
    dfs(arrest[i])  # 변환 후 DFS 실행

print(v.count(1))  # 마약 공급 표시 리스트에서 여전히 마약을 공급 받는 마약 공급책의 수를 count 후 출력
