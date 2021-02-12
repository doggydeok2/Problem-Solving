import sys
input = sys.stdin.readline

n = int(input())
s = [0] * 50001
cnt = ptr = 0

for i in range(n):
    x, y = map(int, input().split())
    while ptr and y < s[ptr]:
        cnt += 1
        ptr -= 1
    if y > s[ptr]:
        ptr += 1
        s[ptr] = y

print(cnt + ptr)
