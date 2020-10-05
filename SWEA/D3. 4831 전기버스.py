T = int(input())
 
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
 
    elec = K  # 최대 이동할 수 있는 정류장
    charge = 0  # 충전횟수
    chk = 0 # 지나간 정류장
 
    for i in range(1, N):
        elec -= 1
        if elec < 0:
            charge = 0
            break
        if charge < M and arr[chk] == i:
            chk += 1
            try:
                arr[chk] - i > elec
            except:
                chk -= 1
                arr[chk] = N
            if arr[chk] - i > elec:
                charge += 1
                elec = K
 
    print(f'#{tc} {charge}')