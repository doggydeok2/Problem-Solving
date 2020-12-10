N = int(input())
cnt = 0
n = 666
while True:
    if '666' in str(n):
        cnt += 1
        if cnt == N: break
    n += 1
print(n)