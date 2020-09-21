def ins(pos, row, ptr):  # 현재 위치, 다음 새 리스트 삽입 위치, 현재 먹이 정보 인덱스
    global trie
    if ptr == data[0] + 1: return r  # 먹이 정보를 다 확인했으면 다음 리스트 삽입 위치 반환
    for ch in trie[pos]:  # 트라이의 먹이 정보들에 대하여 반복
        if ch[0] == data[ptr]:  # 현재 트라이에 먹이 정보가 존재한다면
            return ins(ch[1], row, ptr + 1)  # 그 먹이 정보에 저장된 다음 위치로 이동
    trie[pos] += [[data[ptr], row]]  # 트라이에 먹이 정보가 없었다면 새로 추가
    trie += [[]]  # 새로 추가한 먹이 정보가 가질 하위 항목 리스트 생성
    return ins(row, row + 1, ptr + 1)  # 새로 추가한 먹이 정보에 저장된 다음 위치로 이동


def pr(row, floor):  # 현재 trie 위치, 내려온 지하 층수
    for ch in trie[row]:  # 현재 trie를 순회하며
        print('--' * floor, end = '')  # 내려온 층수만큼 --를 출력하고
        print(ch[0])  # 그 끝에 먹이 종류를 출력
        pr(ch[1], floor + 1)  # DFS로 하위 항목들을 연달아 출력


N = int(input())  # 먹이 정보 수
trie = [[]]  # 트라이를 이차원 배열로 초기화
r = 1  # 새 방의 위치로 사용할 인덱스
for _ in range(N):  # 먹이 정보 수만큼 반복
    data = list(input().split())  # 데이터는 공백으로 나눈 str 형태로 저장
    # data[0] 만큼의 dfs
    data[0] = int(data[0])  # data의 첫 입력은 먹이 정보 갯수이므로 int 형변환
    r = ins(0, r, 1)  # 굴을 입력하는 dfs 진행

# 정렬 후 출력
for li in tries:
    li.sort()  # 하위 항목별로 각각 알파벳순 정렬
pr(0, 0)  # 출력