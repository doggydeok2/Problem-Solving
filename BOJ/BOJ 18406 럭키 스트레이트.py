N = input()  # 수는 자르기 쉽도록 str 형태로 받음
l, r = 0, 0  # 왼쪽, 오른쪽
for i in range(len(N) // 2):  # 왼쪽과 오른쪽의 수를 더해나감
    l += int(N[i])
    r += int(N[-(i + 1)])

if l == r: print('LUCKY')  # 같으면 럭키 아니면 레디
else: print('READY')