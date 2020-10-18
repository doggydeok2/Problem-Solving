
# 1. 앞에서부터 더해가는 부분합 219 ms
# def subset(s, n):  # s: 현재 키의 합, n: 현재 처리중인 사람의 번호
#     global gapMin
#     if s >= B:  # 키의 합이 선반 높이를 넘어섰다면 그 차이를 갱신
#         gapMin = s - B if s >= B and gapMin > s - B else gapMin
#     elif n == N: pass  # 모든 사람을 확인하고도 선반에 모자란 경우는 무시
#     else:  # 이외의 경우 subset을 계속 진행
#         subset(s, n + 1)
#         subset(s + hs[n], n + 1)

# T = int(input())
#     for tc in range(1, T + 1):
#         N, B = map(int, input().split())
#         hs = list(map(int, input().split()))
#         gapMin = 200000  # 키는 최대 1만이며 20명이 존재
    
#         subset(0, 0)
#         print(f'#{tc} {gapMin}')

# 2. 앞에서부터 빼가는 부분합 180 ms
def subset(s, n):  # s: 현재 키의 합, n: 현재 처리중인 사람의 번호
    global gapMin
    if s >= B and n != N:  # 키의 합이 선반 높이를 넘어선 상태고 남은 사람이 있다면
        subset(s, n + 1)  # 사람을 빼지 않은 subset
        ts = s - hs[n]  # 사람을 뺐을 경우 키의 합
        if ts >= B:  # 사람을 빼고도 선반보다 키의 합이 더 크다면
            gapMin = ts - B if gapMin > ts - B else gapMin  # 차이를 갱신
            subset(ts, n + 1)  # 줄어든 키의 합으로 subset


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    hs = list(map(int, input().split()))
    S = sum(hs)  # 키의 합을 별도로 구해야 이후 사람을 하나씩 제거할 수 있음
    gapMin = S - B  # 차이의 최대는 키의 합에서 선반의 길이를 뺀 경우이므로 그 값으로 초기화

    subset(S, 0)
    print(f'#{tc} {gapMin}')
