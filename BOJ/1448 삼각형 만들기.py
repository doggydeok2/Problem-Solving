import sys
input = sys.stdin.readline

N = int(input())
straws = [int(input()) for _ in range(N)]
straws.sort(reverse=True)
maxLength = -1
for i in range(1, N - 1):
    if straws[i - 1] < straws[i] + straws[i + 1]:
        maxLength = straws[i] + straws[i - 1] + straws[i + 1]
        break
print(maxLength)