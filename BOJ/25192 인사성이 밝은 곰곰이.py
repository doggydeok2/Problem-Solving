import collections
import sys
rl = sys.stdin.readline


N = int(input())
cnt = 0
user_dict = collections.defaultdict(int)
for _ in range(N):
    cmd = rl().rstrip()
    if cmd == "ENTER":
        cnt += len(user_dict)
        user_dict.clear()
    else:
        user_dict[cmd] += 1
print(cnt + len(user_dict))
