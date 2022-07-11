import sys


N = int(input())
ans = cnt = 0
num = ''
for val in sys.stdin.read():
    if val == ' ' or val == '\n':
        ans += int(num) - cnt
        cnt += 1
        num = ''
    else:
        num += val
print(ans)
