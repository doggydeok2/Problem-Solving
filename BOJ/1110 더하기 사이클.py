N = int(input())
cnt, Ntemp = 0, N
while True:
    Ntemp = ((Ntemp % 10) * 10 + (Ntemp // 10 + Ntemp % 10) % 10)
    cnt += 1
    if Ntemp == N: break
print(cnt)